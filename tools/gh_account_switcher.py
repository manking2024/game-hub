#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gh_account_switcher.py — GitHub 账号一键切换器（Tkinter 桌面工具，零第三方依赖）。

双击启动（或 python tools/gh_account_switcher.py）：窗口里点账号即切换，
不用再手动敲 gh auth switch 命令。

命令行自检（无窗口）:
    python tools/gh_account_switcher.py --check     # 显示当前账号与可用账号
"""
import os
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox

GH = r"C:\Program Files\GitHub CLI\gh.exe"
PROXY = "http://127.0.0.1:7890"

# 账号 → 用途说明（按实际需要增改）
ACCOUNTS = [
    ("manking2024", "游戏站 GameHub"),
    ("chuangyeli", "资源导航站"),
]

BG = "#f6f7f9"
FG = "#2b2f36"
GREEN = "#1f3b2c"
GREEN_LIGHT = "#e8f5e9"
GRAY = "#8a8f98"


def gh(*args, timeout=30):
    """调用 gh 命令，自动带上代理环境变量。"""
    env = dict(os.environ)
    env["HTTPS_PROXY"] = PROXY
    env["HTTP_PROXY"] = PROXY
    try:
        p = subprocess.run(
            [GH, *args], capture_output=True, text=True,
            encoding="utf-8", errors="replace", env=env, timeout=timeout,
        )
        return p.returncode, (p.stdout + p.stderr).strip()
    except FileNotFoundError:
        return 127, f"未找到 gh：{GH}"
    except Exception as exc:  # noqa: BLE001
        return 1, str(exc)


def current_account():
    code, out = gh("api", "user", "--jq", ".login")
    return out if code == 0 else None


def list_accounts():
    code, out = gh("auth", "status")
    if code != 0:
        return []
    accounts = []
    for line in out.splitlines():
        if "account" in line and "Logged in" in line:
            # 形如: ✓ Logged in to github.com account manking2024 (keyring)
            parts = line.split("account")
            if len(parts) > 1:
                accounts.append(parts[1].split()[0])
    return accounts


class SwitcherApp:
    def __init__(self, root):
        self.root = root
        root.title("GitHub 账号切换器")
        root.geometry("440x360")
        root.configure(bg=BG)
        root.resizable(False, False)

        header = tk.Frame(root, bg=GREEN)
        header.pack(fill="x")
        tk.Label(header, text="GitHub 账号切换器", bg=GREEN, fg="white",
                 font=("Microsoft YaHei", 15, "bold")).pack(pady=(14, 2))
        tk.Label(header, text="点一下账号，切换推送身份", bg=GREEN, fg="#cde8d4",
                 font=("Microsoft YaHei", 10)).pack(pady=(0, 14))

        # 当前账号状态区
        self.status_box = tk.Frame(root, bg=GREEN_LIGHT, padx=12, pady=8)
        self.status_box.pack(fill="x", padx=16, pady=12)
        self.current_lbl = tk.Label(self.status_box, text="读取中…", bg=GREEN_LIGHT,
                                    font=("Microsoft YaHei", 12, "bold"), fg=FG)
        self.current_lbl.pack()

        # 账号按钮区
        btn_area = tk.Frame(root, bg=BG)
        btn_area.pack(fill="both", expand=True, padx=16)
        self.buttons = {}
        for account, purpose in ACCOUNTS:
            btn = tk.Button(
                btn_area, text=f"{account}\n（{purpose}）", font=("Microsoft YaHei", 12, "bold"),
                bg="#ffffff", fg=FG, activebackground="#dcedc8", relief="flat",
                bd=1, highlightthickness=1, cursor="hand2",
                command=lambda a=account: self.switch(a),
            )
            btn.pack(fill="x", pady=6, ipady=14)
            self.buttons[account] = btn

        # 底部操作
        foot = tk.Frame(root, bg=BG)
        foot.pack(fill="x", padx=16, pady=10)
        self.msg_lbl = tk.Label(foot, text="", bg=BG, fg=GRAY, font=("Microsoft YaHei", 9))
        self.msg_lbl.pack(side="left")
        tk.Button(foot, text="刷新状态", font=("Microsoft YaHei", 9),
                  bg="#ffffff", relief="flat", command=self.refresh).pack(side="right")

        self.refresh()

    def refresh(self):
        acc = current_account()
        self.current = acc
        if acc:
            purpose = dict(ACCOUNTS).get(acc, "")
            self.current_lbl.config(text=f"当前账号：{acc}" + (f"（{purpose}）" if purpose else ""))
            for acct, btn in self.buttons.items():
                if acct == acc:
                    btn.config(bg="#c8e6c9", state="disabled")
                else:
                    btn.config(bg="#ffffff", state="normal")
        else:
            self.current_lbl.config(text="未检测到已登录账号")
        self.msg_lbl.config(text="")

    def switch(self, account):
        if account == self.current:
            self.msg_lbl.config(text="已经是当前账号")
            return
        self.msg_lbl.config(text=f"正在切换到 {account} …")
        self.root.update()
        code, out = gh("auth", "switch", "--user", account)
        if code == 0:
            self.refresh()
            self.msg_lbl.config(text=f"✅ 已切换到 {account}")
        else:
            self.msg_lbl.config(text="")
            messagebox.showerror("切换失败", out or f"切换 {account} 失败，请检查 gh 登录状态")


def main():
    if "--check" in sys.argv:
        acc = current_account()
        print("当前账号:", acc if acc else "未知/未登录")
        print("可用账号:", ", ".join(list_accounts()) or "无")
        return 0
    root = tk.Tk()
    SwitcherApp(root)
    root.mainloop()
    return 0


if __name__ == "__main__":
    sys.exit(main())
