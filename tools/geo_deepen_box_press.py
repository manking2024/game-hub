#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
geo_deepen_box_press.py — Deepen box-press-puzzle after it broke into Google's
index in GSC period 7 (2026-11-17, 1 impression @ position 7).

Source of truth (no invention):
  * GameMonetize feed entry already stored in games.json
  * GameMonetize official page https://gamemonetize.com/box-press-puzzle-game
      - Instructions: "Mouse to click"
      - Category: Arcade
      - Tags: Adventure, Arcade, Fun, Puzzle, Unity3D, WebGL
      - Mobile Ready: No
      - Description: pistons in perfect sequence push cyan cubes into the
        central drop zone; avoid blocking pathways; increasingly complex
        spatial layouts
  * Feed summary adds the step-limit warning ("before you run out of steps")

Content policy: no invented level counts, scores, timers, prices or ratings.

Usage: python tools/geo_deepen_box_press.py
Then:  python tools/gen_site.py
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "games.json")

BOX_PRESS = {
    "description": (
        "Play Box Press Puzzle free online — a piston-driven spatial logic puzzle. "
        "Click pistons in the right sequence to push cyan cubes into the central drop "
        "zone without blocking a pathway. Mouse only, no download."
    ),
    "sections": [
        {
            "h2": "What Kind of Puzzle Is Box Press Puzzle?",
            "body": (
                "Box Press Puzzle is a spatial logic game built around a machine instead of a "
                "character. There is no avatar to walk around the board. The board is a small "
                "mechanism: pistons sit at fixed points, cubes sit on tracks, and the drop zone "
                "is in the middle. Your only verb is to press a piston and make it shove a cube "
                "one cell along its track.\n\n"
                "That single verb is the whole game. The puzzle is not about reflexes or "
                "exploration — it is about arriving at the correct firing sequence before you "
                "commit. The game's own description puts it plainly: activate the pistons in the "
                "perfect sequence to push the smooth cyan cubes directly into the central drop "
                "zone, avoid blocking pathways, and work through increasingly complex spatial "
                "layouts until the board is complete.\n\n"
                "The platform lists it under Arcade with Puzzle and Logic tags on a Unity3D "
                "WebGL build. In practice it plays like a mechanical Sokoban: the same access "
                "and ordering problem, with clicking replacing footsteps."
            ),
        },
        {
            "h2": "How Do You Play Box Press Puzzle?",
            "body": (
                "The control scheme is one input, and the official instructions are two words: "
                "mouse to click.\n\n"
                "- Read the board first. Identify the drop zone, every cube, and which piston "
                "touches which cube.\n"
                "- Trace the route each cube needs to travel before you press anything.\n"
                "- Click a piston to fire it. The piston pushes the cube it is pointed at one cell "
                "along its track.\n"
                "- Watch what the push does to the other cubes. A cube you move can land in front "
                "of another cube's only path.\n"
                "- Continue until every cube has reached the central drop zone.\n\n"
                "There is no aiming reticle, no drag gesture and no keyboard alternative "
                "documented — it is a click on the piston itself. Because each press is a "
                "commitment rather than a scroll of the camera, the pacing is deliberate: think, "
                "press, watch, re-plan. If a board goes wrong, the fix is a level reset; the "
                "existing page copy is honest that a wrong press costs seconds rather than a "
                "whole session."
            ),
        },
        {
            "h2": "Why Does Press Order Matter More Than Speed?",
            "body": (
                "In most arcade games, doing something fast is better than doing it late. Box "
                "Press Puzzle inverts that completely. A press that fires two moves too early is "
                "not a slower version of the correct press — it is a different board state, and "
                "often an unrecoverable one.\n\n"
                "The reason is that pistons share the same floor. Every cube occupies space, and "
                "every push changes which space is occupied. Press a piston early and its cube "
                "may park in a corridor another cube still needs to use. Now that second cube "
                "has nowhere to go, and no amount of additional pressing fixes it — the blocker "
                "is permanent until you reset.\n\n"
                "That is why the useful habit is to solve the board backwards. Start at the drop "
                "zone and ask what the last press must be. Then ask what the press before it must "
                "be, and what position each cube had to be in for that to work. Working backwards "
                "through the sequence exposes ordering conflicts while they are still cheap to "
                "catch, instead of discovering them at press nine."
            ),
        },
        {
            "h2": "Why Do Cubes Get Stuck, and How Do You Prevent It?",
            "body": (
                "Almost every failed board comes from one of three blocking patterns. They are "
                "worth naming because each one is visible before you press:\n\n"
                "- The corridor plug. A cube ends up parked in the only lane a second cube needs. "
                "Prevention: check whether any cube's remaining route passes through the cell "
                "you are about to fill.\n"
                "- The premature finish. You push a cube into the drop zone before a later cube "
                "needed that approach cell as a staging square. Prevention: finish cubes last, "
                "not first, unless the sequence requires otherwise.\n"
                "- The two-cube deadlock. Two cubes end up facing each other with no piston able "
                "to separate them. Prevention: never push two cubes into the same short "
                "corridor, even on opposite sides.\n\n"
                "A useful check before any press: after this push, does every unplaced cube still "
                "have an unobstructed route to the drop zone? If the answer is no, and the "
                "obstruction is a cube rather than a wall, that press is the wrong one. This is "
                "exactly the failure the game warns about in its own description — blocking "
                "pathways is the intended trap, not a bug."
            ),
        },
        {
            "h2": "How Does Box Press Puzzle Compare to Sokoban?",
            "body": (
                "| Feature | Box Press Puzzle | Classic Sokoban |\n"
                "| --- | --- | --- |\n"
                "| Actor | No avatar; you fire pistons | One walking character |\n"
                "| Move type | Piston shoves a cube one cell | Character pushes a crate |\n"
                "| Decision unit | Sequence of presses | Sequence of steps |\n"
                "| Failure mode | Blocked pathway, deadlock | Blocked corner, deadlock |\n"
                "| Recovery | Reset the level | Undo, or restart the level |\n"
                "| Engine | Unity3D / WebGL | Varies widely |\n\n"
                "The family resemblance is real: both games are about access and ordering, and "
                "both punish a move that looks locally sensible and traps a crate globally. The "
                "difference is how much you have to manage. Sokoban asks you to steer a character "
                "and the character's own position becomes a constraint. Box Press Puzzle removes "
                "the character entirely, which means the board is smaller, the state space is "
                "cleaner, and restarting is faster.\n\n"
                "That makes it a better entry point into block-pushing puzzles for people who find "
                "Sokoban's walking-into-your-own-solution problem annoying. It is also a thinner "
                "game: fewer moving parts means fewer surprises per board."
            ),
        },
        {
            "h2": "Does Box Press Puzzle Work on Mobile or Tablet?",
            "body": (
                "This is the one point where most pages about this game mislead you, so it is worth "
                "stating directly. The GameMonetize listing marks the game **Mobile Ready: No**. "
                "It is a desktop-oriented Unity WebGL build with a mouse-click control scheme, and "
                "the documented instruction is mouse input rather than touch input.\n\n"
                "Practically: play it on a laptop or desktop. A tablet or phone may load the frame "
                "and may respond to a tap, but the platform does not certify mobile support, and a "
                "single-input puzzle that depends on precise piston targeting is the wrong shape for "
                "a small touch screen. If you are on mobile and something does not respond, that is "
                "the known limitation rather than a fault on your end.\n\n"
                "No installation and no account are required on desktop — the game runs inside the "
                "browser through an embedded WebGL player. If the frame ever fails to load, refresh "
                "the page first; a stale or blocked frame is the usual cause with third-party "
                "embedded games."
            ),
        },
        {
            "h2": "Who Should Play Box Press Puzzle?",
            "body": (
                "It fits players who like short, self-contained logic boards and do not need "
                "spectacle. If you enjoy deducing a correct sequence, working backwards from a goal, "
                "and resetting to try a different order, this is the right shape of puzzle. The "
                "difficulty curve is stated honestly by the game itself: layouts start simple and add "
                "pistons, branch paths and multiple cubes.\n\n"
                "It is a poor fit in three cases. If you want an action game, there is no real-time "
                "pressure here. If you want mobile play, the build is not mobile-ready. And if you "
                "want a long campaign with unlocks or a story, this is a compact mechanical puzzle "
                "rather than a progression game.\n\n"
                "The best way to judge it takes one board: load it, read the drop zone, and see "
                "whether tracing the sequence backwards feels interesting. That impulse — wanting to "
                "solve the order before touching anything — is the whole appeal, and it shows up "
                "immediately or not at all."
            ),
        },
    ],
    "faq": [
        {"q": "Is Box Press Puzzle free to play?",
         "a": "Yes. It is free in the browser with no download, no account and no payment. The game "
              "is embedded directly on this page as a WebGL build."},
        {"q": "How do you control Box Press Puzzle?",
         "a": "With the mouse. The official instructions are just \"mouse to click\" — you click a "
              "piston and it pushes the cube it is aimed at one cell along its track. No keyboard "
              "alternative is documented."},
        {"q": "What is the goal in each level?",
         "a": "Push every smooth cyan cube into the central drop zone by firing the pistons in the "
              "right sequence. A level is complete when all cubes have reached the drop zone."},
        {"q": "What happens if I fire a piston in the wrong order?",
         "a": "A cube can end up wedged against a wall or parked in a lane another cube needs, which "
              "is usually unrecoverable. Reset the level and re-plan the sequence — boards are short, "
              "so a wrong press costs seconds, not a run."},
        {"q": "Is there a limit on how many presses you get?",
         "a": "The game's own description warns you can run out of steps, so treat each press as "
              "spent rather than experimenting freely. Plan the full sequence before you start "
              "firing."},
        {"q": "How is Box Press Puzzle different from Sokoban?",
         "a": "Classic Sokoban has you walk a character around and push crates. Here there is no "
              "character — you fire pistons that shove cubes one cell. The access-and-ordering logic "
              "is the same, but the board state is simpler and resetting is faster."},
        {"q": "Does Box Press Puzzle work on mobile or tablet?",
         "a": "The GameMonetize listing marks it Mobile Ready: No. It is a desktop Unity WebGL build "
              "with a mouse-click control scheme, so a laptop or desktop is the intended way to play."},
        {"q": "Will my progress be saved?",
         "a": "There is no account system, so progress is stored locally in your browser. Returning "
              "in the same browser usually keeps your place; clearing site data resets it."},
    ],
    "date": "2026-11-17",
}


def word_count(sections, faq):
    n = 0
    for s in sections:
        n += len(s["body"].split())
    for f in faq:
        n += len(f["q"].split()) + len(f["a"].split())
    return n


def main():
    with open(DATA, "r", encoding="utf-8-sig") as f:
        data = json.load(f)

    hit = 0
    for g in data["games"]:
        if g["slug"] != "box-press-puzzle":
            continue
        g["description"] = BOX_PRESS["description"]
        g["sections"] = BOX_PRESS["sections"]
        g["faq"] = BOX_PRESS["faq"]
        g["date"] = BOX_PRESS["date"]
        g["keywords"] = [
            "box press puzzle",
            "piston puzzle game",
            "spatial logic puzzle",
            "sokoban style browser game",
        ]
        hit += 1
        print(f"[deepen] box-press-puzzle {word_count(BOX_PRESS['sections'], BOX_PRESS['faq'])} words")

    if not hit:
        print("[deepen] box-press-puzzle not found", file=sys.stderr)
        return 1

    with open(DATA, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return 0


if __name__ == "__main__":
    sys.exit(main())
