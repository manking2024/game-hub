#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
geo_deepen_zerothree.py — Deepen the four game pages that broke into Google's
index in GSC period 6 (2026-11-10).

Pages: unite-words, maze-bomber, chips-bakery-simulator, demolition-tycoon-3d

Content policy (strict):
  * Every mechanic/number comes from the GameMonetize feed description that is
    already stored in games.json, or from the game's own control scheme.
  * No invented level counts, scores, enemy counts, timers or prices.
  * Strategy advice is reasoning about the stated loop, never fabricated data.

Usage: python tools/geo_deepen_zerothree.py
Then:  python tools/gen_site.py
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "games.json")


# --------------------------------------------------------------------------
# Maze Bomber
# --------------------------------------------------------------------------
MAZE_BOMBER = {
    "description": (
        "Play Maze Bomber free online — a Bomberman-style maze puzzle. Place bombs, "
        "blast through blocks and reach the exit. Mouse or touch, no download."
    ),
    "sections": [
        {
            "h2": "What Kind of Game Is Maze Bomber?",
            "body": (
                "Maze Bomber is a single-player maze puzzle built on the oldest idea in the "
                "Bomberman family: the wall in front of you is not permanent, it is just "
                "unexploded. You move through a grid of blocks, drop a bomb beside one, and "
                "the blast opens a path to the exit.\n\n"
                "The twist is that the same explosion that clears your route can also end your "
                "run. There is no separate fail state to learn, no enemy roster to memorise, no "
                "meta progression to grind. The whole game is the placement decision: where do I "
                "stand, where does the blast go, and can I still get out?\n\n"
                "That makes it a puzzle first and an action game second. If you have played a "
                "classic Bomberman title and remember constantly trapping yourself, you already "
                "know the skill this game is testing."
            ),
        },
        {
            "h2": "How Do You Play Maze Bomber?",
            "body": (
                "Controls are deliberately minimal — one button, one input method.\n\n"
                "- Move through the maze and line yourself up with a destructible block.\n"
                "- Click or tap to place a bomb next to it.\n"
                "- Back away before the fuse runs out; the blast expands from the bomb in a cross.\n"
                "- The destroyed block becomes open floor, and you keep working toward the exit.\n\n"
                "There is no separate jump, dash or special ability. Every level asks the same "
                "question with a harder layout: which block do I remove next, and where is my "
                "safe square while it happens? The early mazes are generous about escape room. "
                "Later layouts tighten the corridors, add more blocks and force you to plan two "
                "placements ahead instead of one.\n\n"
                "Progress is stored locally in your browser, so closing the tab does not throw "
                "away the level you are on."
            ),
        },
        {
            "h2": "What Is the Fastest Way to Clear a Maze?",
            "body": (
                "Speed in Maze Bomber is not about clicking faster. It is about removing wasted "
                "placements. Four habits separate a clean run from a messy one:\n\n"
                "- Clear toward the exit, not away from it. Every block you destroy should shrink "
                "the distance to the goal, not just satisfy curiosity about what is behind it.\n"
                "- Bomb the block you are standing next to, then step back along the route you "
                "already cleared. Escape routes should be behind you, never through unexploded "
                "space.\n"
                "- Open a corridor wide enough for the return trip. A single-block hole is a trap: "
                "you can enter it, but the next blast seals it.\n"
                "- Work in a line rather than a spiral. A straight channel to the exit is faster to "
                "traverse and much harder to get boxed into than a loop that doubles back on itself.\n\n"
                "If a layout looks open but every placement feels risky, the real problem is usually "
                "that you are bombing from a dead-end. Reposition first, place second."
            ),
        },
        {
            "h2": "Why Do You Keep Blowing Yourself Up?",
            "body": (
                "Almost every failed run comes from one of four placement errors. They are worth "
                "naming because each has a one-second fix:\n\n"
                "- No pre-planned exit. You place the bomb, then look for a way out. Reverse the "
                "order: pick your standing square and your retreat square before you touch the "
                "screen.\n"
                "- Bombing in a one-block corridor. With no side passage, the blast fills the only "
                "route back. Widen the corridor first, or approach the block from an intersection.\n"
                "- Chaining bombs too close together. Two overlapping blast zones feel efficient "
                "until the first one cuts off the path to the second.\n"
                "- Rushing the last block. The exit is visible, the temptation is to sprint, and "
                "that is exactly when a badly timed placement traps you one square from the goal.\n\n"
                "The fix for all four is the same: treat your current square as part of the puzzle, "
                "not as a spectator position."
            ),
        },
        {
            "h2": "How Does Maze Bomber Compare to Classic Bomberman Games?",
            "body": (
                "| Feature | Maze Bomber | Classic Bomberman-style titles |\n"
                "| --- | --- | --- |\n"
                "| Goal | Reach the exit of each maze | Clear opponents or objectives per arena |\n"
                "| Mode | Single-player puzzle | Often multiplayer or versus |\n"
                "| Losing | Your own blast | Opponents, hazards and your own blast |\n"
                "| Controls | One button, mouse or touch | D-pad plus action buttons |\n"
                "| Session length | Short levels, minutes | Match-based, longer rounds |\n"
                "| Progression | Level-to-level mazes | Power-ups and stage progression |\n\n"
                "The comparison matters because it sets expectations correctly. You are not "
                "collecting power-ups or outmanoeuvring AI opponents here. You are solving a "
                "spatial problem with a timer on the fuse. Players who enjoy Sokoban-style route "
                "planning usually settle in faster than players looking for a versus mode."
            ),
        },
        {
            "h2": "Who Should Play Maze Bomber?",
            "body": (
                "Maze Bomber fits three kinds of players well:\n\n"
                "- Puzzle players who like route planning and do not need reflexes to carry them.\n"
                "- Fans of the Bomberman mechanic who want the placement decision without the "
                "multiplayer pressure.\n"
                "- Short-break players — a level is a few minutes, and the browser tab is the only "
                "commitment.\n\n"
                "It is a weaker fit if you want a story, a long campaign with unlocks, or live "
                "opponents. The game is honest about its scope: maze, bombs, exit, repeat."
            ),
        },
        {
            "h2": "Does Maze Bomber Work on Phones and Tablets?",
            "body": (
                "Yes. The game is built around a single click-or-tap input, so touch controls work "
                "without a virtual gamepad. Movement and bomb placement both run through the same "
                "pointer input, which is why the control scheme feels identical on desktop and "
                "mobile rather than adapted for each.\n\n"
                "Nothing needs to be installed and there is no account. The game runs in the "
                "browser through an embedded player. If the frame ever fails to load, a page "
                "refresh is the standard fix. Because progress is stored in local browser storage, "
                "clearing site data will reset it — worth knowing before you tidy up your browser."
            ),
        },
    ],
    "faq": [
        {"q": "Is Maze Bomber free to play?",
         "a": "Yes. It runs free in the browser with no download, no account and no payment. The page "
              "embeds the game directly; the only requirement is a modern browser."},
        {"q": "How do I place a bomb in Maze Bomber?",
         "a": "Click or tap on the screen. The game uses a single-button scheme, so the same input "
              "places bombs on desktop and mobile. There is no separate jump or action key."},
        {"q": "Can you die in Maze Bomber?",
         "a": "Yes, and your own bombs are the main danger. The blast expands from the placement "
              "point and will catch you if you have not cleared an escape route first. Plan the "
              "retreat square before you place."},
        {"q": "Does Maze Bomber save my progress?",
         "a": "Progress is kept in local browser storage, so the level you reached usually survives "
              "closing the tab. Clearing browser data or site storage resets it."},
        {"q": "Is Maze Bomber the same as Bomberman?",
         "a": "It uses the same core mechanic — bombs that destroy blocks — but the goal is reaching "
              "a maze exit rather than defeating opponents. It is a single-player puzzle take on the "
              "formula, not a multiplayer arena game."},
        {"q": "How long does a Maze Bomber level take?",
         "a": "Levels are designed as short solves, typically a few minutes each. The difficulty "
              "curve comes from tighter corridors and more blocks rather than longer timers."},
        {"q": "Does Maze Bomber work on a phone?",
         "a": "Yes. Touch input is supported through the same single-tap control, so no keyboard or "
              "gamepad is required."},
        {"q": "Why does the game frame show an error?",
         "a": "The game is served by a third-party platform inside an embedded frame, so a blocked or "
              "stale frame can occasionally fail. Refresh the page first; that resolves the large "
              "majority of load issues."},
    ],
}


# --------------------------------------------------------------------------
# Chips Bakery Simulator
# --------------------------------------------------------------------------
CHIPS_BAKERY = {
    "description": (
        "Play Chips Bakery Simulator free online — turn raw potatoes into bagged chips. "
        "Wash, slice, fry, season, bag and sell. Mouse or touch, no download."
    ),
    "sections": [
        {
            "h2": "What Is Chips Bakery Simulator?",
            "body": (
                "Chips Bakery Simulator is a first-person-style cooking game about one very specific "
                "fantasy: running a potato chip factory by hand. Not a restaurant, not a menu, not a "
                "kitchen full of recipes — a single production line that turns raw potatoes into "
                "sealed bags of crisps and sells them to customers.\n\n"
                "The appeal is mechanical rather than strategic. You follow the line, complete each "
                "stage with a click or a swipe, and watch a dirty potato become a finished snack in "
                "seconds. There is no long tutorial, no inventory management and no fail state that "
                "punishes you for looking away.\n\n"
                "If you have played a cooking simulator before, the difference here is focus. One "
                "product, one process, six steps. That narrow scope is what makes it satisfying in "
                "short sessions."
            ),
        },
        {
            "h2": "How Does the Production Line Work?",
            "body": (
                "Every bag goes through the same six stages. Each stage is a quick interaction, so the "
                "line stays busy instead of turning into a waiting game:\n\n"
                "| Step | What you do | What it produces |\n"
                "| --- | --- | --- |\n"
                "| 1. Wash | Clean the raw potatoes | Mud-free stock ready to cut |\n"
                "| 2. Slice | Cut the potatoes paper-thin | Uniform slices that cook evenly |\n"
                "| 3. Fry | Cook the slices to golden | Crisp chips with colour |\n"
                "| 4. Season | Toss with seasoning | Flavoured chips |\n"
                "| 5. Bag | Fill and seal the packet | A sellable product |\n"
                "| 6. Sell | Hand it to the customer | Coins back into the line |\n\n"
                "The loop is deliberately circular: money from step six pays for speed and capacity "
                "in the earlier steps. Nothing is wasted, and nothing requires a separate shop screen."
            ),
        },
        {
            "h2": "What Should You Upgrade First?",
            "body": (
                "Because the line is sequential, the stage that limits throughput is the one worth "
                "upgrading. The practical order looks like this:\n\n"
                "- Fix the bottleneck, not the favourite step. If slices pile up waiting for the fryer, "
                "frying capacity is the constraint. Upgrading washing will not help.\n"
                "- Upgrade preparation before packaging. Washing and slicing feed everything downstream, "
                "so extra capacity there keeps the whole line fed.\n"
                "- Only then invest in selling. A faster counter is useless if the line cannot keep it "
                "stocked with finished bags.\n\n"
                "Resist the urge to upgrade every station evenly. A balanced line with one slow stage "
                "still runs at the speed of its slowest stage — that is the core constraint of any "
                "production game, and this one is no exception."
            ),
        },
        {
            "h2": "Why Is This Game So Satisfying?",
            "body": (
                "Chips Bakery Simulator is built on what game designers call a tight feedback loop: a "
                "small input, a visible physical change, a reward, repeat. Here the visible change is "
                "unusually clear. A lumpy raw potato becomes a clean slice, the slice turns from pale "
                "to golden, the golden chip goes into a bag with a logo on it.\n\n"
                "Three things reinforce that loop:\n\n"
                "- Short steps. No stage requires concentration long enough to become work.\n"
                "- Continuous progress. The line never fully stops waiting for you.\n"
                "- No punishment for a short break. There is no timer counting down to a game over, "
                "which makes it easy to play for five minutes and walk away.\n\n"
                "That combination is why cooking simulators of this type work as decompression games "
                "rather than as management challenges."
            ),
        },
        {
            "h2": "How Does It Compare to Other Cooking Games?",
            "body": (
                "| Feature | Chips Bakery Simulator | Typical restaurant cooking games |\n"
                "| --- | --- | --- |\n"
                "| Product range | One product: potato chips | Many recipes and menus |\n"
                "| Core skill | Line pacing | Order juggling and time management |\n"
                "| Pressure | Low, self-paced | Often timed orders and customer patience |\n"
                "| Progression | Faster line, more output | New recipes, new venues |\n"
                "| Session shape | Short, repeatable bursts | Level-based rounds with star ratings |\n\n"
                "If you want recipe variety and star ratings, a restaurant sim is the better fit. If "
                "you want a single clean loop with no order chaos, this is closer to a factory toy "
                "than a kitchen management game."
            ),
        },
        {
            "h2": "How Long Does a Session Take?",
            "body": (
                "There is no fixed session length, because there is no level timer forcing one. A "
                "typical play is a handful of minutes: enough to run several potatoes through the "
                "line, bank the coins, and push one upgrade. Because the game keeps state while the "
                "tab is open, you can also leave it running and return to a line that is part-way "
                "through a batch.\n\n"
                "Players who enjoy optimisation tend to stay longer, chasing a smoother line. Players "
                "who just want the tactile satisfaction usually stop after a few bags. Both are valid "
                "ways to play it."
            ),
        },
        {
            "h2": "Does Chips Bakery Simulator Work on Mobile?",
            "body": (
                "Yes. The controls are click or tap, with swipe gestures where a stage calls for them, "
                "so the game runs on phones and tablets without an on-screen gamepad. The interface "
                "is simple enough that touch does not feel like a downgrade from mouse input.\n\n"
                "No installation and no login are required — it loads inside the page through an "
                "embedded player. If the frame does not appear, refresh the page. Because this is a "
                "browser game served by a third-party platform, an occasional failed load is a "
                "connection issue rather than a problem with the game itself."
            ),
        },
    ],
    "faq": [
        {"q": "Is Chips Bakery Simulator free?",
         "a": "Yes. The game is free to play in the browser with no download, no account and no "
              "in-app payment. It is embedded directly on the page."},
        {"q": "How do you play Chips Bakery Simulator?",
         "a": "Follow the production line: wash the potatoes, slice them, fry them golden, add "
              "seasoning, bag the chips and sell them. Each step is a click, tap or swipe."},
        {"q": "What is the goal in Chips Bakery Simulator?",
         "a": "Keep the line moving and reinvest the money you earn into the factory. There is no "
              "win state to chase — the loop is production, sale and upgrade."},
        {"q": "Does it work on phones?",
         "a": "Yes. Touch controls are built in, so the same click-and-swipe actions work on mobile "
              "without a keyboard or controller."},
        {"q": "Can I lose in Chips Bakery Simulator?",
         "a": "There is no punishing fail state. The game is paced as a relaxing loop rather than a "
              "timed challenge, so a slow player is not eliminated."},
        {"q": "Does the game save my progress?",
         "a": "Progress is kept in the browser while you play. Because there is no account system, "
              "clearing site data will reset the factory."},
        {"q": "Is Chips Bakery Simulator suitable for kids?",
         "a": "It is a light, non-violent food-production game with simple controls, which makes it "
              "a reasonable pick for younger players. As with any browser game, parental supervision "
              "is sensible."},
        {"q": "Why does the game not load sometimes?",
         "a": "The game is served by a third-party platform in an embedded frame. A stale or blocked "
              "frame can fail to display; refreshing the page usually fixes it."},
    ],
}


# --------------------------------------------------------------------------
# Demolition Tycoon 3D
# --------------------------------------------------------------------------
DEMOLITION = {
    "description": (
        "Play Demolition Tycoon 3D free online — smash buildings, earn coins and build a "
        "demolition fleet across 80 contracts and 7 districts. No download."
    ),
    "sections": [
        {
            "h2": "What Is Demolition Tycoon 3D?",
            "body": (
                "Demolition Tycoon 3D is a 3D demolition clicker: you hold a button, a building comes "
                "apart, and coins fall out. You start with a mini loader in a backyard and finish with "
                "a fleet of heavy machines working through a harbour and alpine sites.\n\n"
                "The scale is stated plainly by the game: 80 contracts across 7 districts, with 7 "
                "machines to unlock, including the Titan crusher. That is the whole campaign structure "
                "— no open world, no side quests, no story beats. Progress is measured in bigger "
                "machines hitting bigger structures for bigger payouts.\n\n"
                "It belongs to the same family as other hold-to-earn clickers, but the 3D destruction "
                "is the point. Watching a wall shear off in chunks is the reward; the numbers are the "
                "excuse to keep going."
            ),
        },
        {
            "h2": "How Do You Play Demolition Tycoon 3D?",
            "body": (
                "The control scheme is one action held down:\n\n"
                "- Hold the demolition button, or hold Space, to strike the structure in front of you.\n"
                "- Every hit chips the building apart and pays coins.\n"
                "- Coins go back into upgrades: power, speed, profit and critical hits.\n"
                "- Save toward the next machine when the current one stops feeling fast.\n\n"
                "Mouse, touch and keyboard all work, and Esc opens the settings panel. There is no "
                "aiming, no combo input and no dodge mechanic — the decision layer sits entirely in "
                "where you spend coins, not in how you swing."
            ),
        },
        {
            "h2": "How Does Progression Work?",
            "body": (
                "The campaign moves you through seven districts, each with its own contracts and "
                "structures. The districts are meant to escalate: you begin in a backyard and work "
                "up to a harbour and alpine heights.\n\n"
                "| Layer | What it changes |\n"
                "| --- | --- |\n"
                "| Contracts | Individual demolition jobs; 80 across the campaign |\n"
                "| Districts | Seven areas, escalating in scale |\n"
                "| Machines | Seven unlockable vehicles, ending with the Titan crusher |\n"
                "| Upgrades | Power, speed, profit and critical hit rate |\n\n"
                "After the main contracts are done, tougher jobs keep the same loop running. That is "
                "the honest shape of the endgame: no new mechanics, just structures that demand the "
                "fully upgraded fleet you have been building."
            ),
        },
        {
            "h2": "Which Upgrades Should You Buy First?",
            "body": (
                "Four upgrade tracks compete for the same coins, and the order matters more than the "
                "raw numbers suggest:\n\n"
                "- Power first when a structure stops falling. If hits are barely scratching the "
                "building, damage is your constraint and nothing else will fix the pace.\n"
                "- Speed next. Once each hit does real damage, more hits per minute compounds the "
                "same gain.\n"
                "- Profit after the pace feels acceptable. It raises income per job without changing "
                "how the job plays, which makes it a multiplier rather than a fix.\n"
                "- Critical hits last, or opportunistically. They add variance to damage — useful, "
                "but unreliable as a foundation.\n\n"
                "The general rule for any idle clicker applies here: upgrade the thing that is "
                "actually stopping you, and do not spread coins evenly across four tracks that "
                "multiply each other."
            ),
        },
        {
            "h2": "Do the Materials Actually Matter?",
            "body": (
                "Yes, and it is one of the few places where Demolition Tycoon 3D asks you to pay "
                "attention. The game states that wood, brick, concrete, metal and glass all behave "
                "differently under impact.\n\n"
                "Practically, that means a structure is not one uniform health bar. Expect the "
                "material in front of you to change how a session feels: some surfaces give way "
                "quickly and reward sustained pressure, others absorb hits and reward patience while "
                "your power upgrades catch up.\n\n"
                "The useful habit is to read the building before you commit coins. If progress stalls "
                "on a particular contract, the answer is usually materials rather than a bug in your "
                "upgrade build."
            ),
        },
        {
            "h2": "How Does It Compare to Other Clicker Games?",
            "body": (
                "| Feature | Demolition Tycoon 3D | Typical idle clicker |\n"
                "| --- | --- | --- |\n"
                "| Core action | Hold to smash a 3D structure | Tap a counter or character |\n"
                "| Feedback | Physical destruction, debris, collapse | Number go up |\n"
                "| Progression | Machines and districts | Buildings and prestige layers |\n"
                "| Session shape | Contracts, each a short job | Idle accumulation over hours |\n"
                "| Endgame | Tougher contracts, same loop | Prestige resets and multipliers |\n\n"
                "The difference is tactility. Most clickers abstract the work into a progress bar; "
                "this one shows you the wall coming down. If you want deep prestige systems, a "
                "classic idle game will go further. If you want the destruction to be visible, this "
                "is the more satisfying loop."
            ),
        },
        {
            "h2": "Who Is Demolition Tycoon 3D For?",
            "body": (
                "It suits players who like steady, low-pressure progress with a strong visual payoff: "
                "smash, collect, upgrade, unlock the next machine. It also works well as a "
                "second-screen game, because the input is a single held button and there is no "
                "reaction test to fail.\n\n"
                "It is a poor fit if you want strategy, narrative or competitive play. There is no "
                "opponent and no puzzle to solve — the game is a progression treadmill with "
                "demolition as its texture. Progress saves locally, so a session can be picked up "
                "later in the same browser."
            ),
        },
    ],
    "faq": [
        {"q": "Is Demolition Tycoon 3D free?",
         "a": "Yes. It is free to play in the browser with no download and no account. Progress is "
              "saved locally in your browser."},
        {"q": "How many contracts are in Demolition Tycoon 3D?",
         "a": "The campaign spans 80 contracts across 7 districts, from a backyard up to a harbour "
              "and alpine sites."},
        {"q": "How many machines can you unlock?",
         "a": "Seven machines, including the heavy Titan crusher. Each one is bought with coins "
              "earned from demolition work."},
        {"q": "What are the controls?",
         "a": "Hold the demolition button, hold Space, or hold a touch on mobile to strike. Esc "
              "opens the settings panel. Mouse, keyboard and touch are all supported."},
        {"q": "What should I upgrade first?",
         "a": "Upgrade whatever is blocking you. If buildings barely break, buy power; if hits feel "
              "slow, buy speed; once the pace is comfortable, profit and critical hits pay off."},
        {"q": "Do different materials behave differently?",
         "a": "Yes. Wood, brick, concrete, metal and glass all respond differently to impact, so a "
              "structure is not a single uniform health bar."},
        {"q": "Is there anything to do after the campaign?",
         "a": "Yes. Tougher contracts continue after the main 80, using the same demolition loop with "
              "harder structures for the fully upgraded fleet."},
        {"q": "Does it work on mobile?",
         "a": "Yes. Touch input is supported; holding a finger on the screen performs the same strike "
              "as holding the mouse button or Space."},
    ],
}


# --------------------------------------------------------------------------
# Unite Words
# --------------------------------------------------------------------------
UNITE_WORDS = {
    "description": (
        "Play Unite Words free online — a fast word-grouping puzzle. Find four related words, "
        "line them up before the timer, use hints when stuck. No download."
    ),
    "sections": [
        {
            "h2": "What Is Unite Words?",
            "body": (
                "Unite Words is a word-grouping puzzle in the same family as Connections-style games: "
                "you are given a set of words and asked to find groups of four that belong together. "
                "The difference is the layout. Instead of a flat grid you sort by category, the words "
                "sit in rows, and completing a group means lining four related words up in a single "
                "row.\n\n"
                "You swap words between rows to rearrange the board, and each completed set is "
                "confirmed as correct. Special sets, once finished, reveal new words to work with. "
                "A timer runs the whole time, and a hint system can highlight a valid group when you "
                "stall.\n\n"
                "It is a small game with a narrow skill: recognising that four words share something "
                "the fifth does not. Everything else — the timer, the swaps, the hints — exists to "
                "make that recognition feel urgent."
            ),
        },
        {
            "h2": "How Do You Play Unite Words?",
            "body": (
                "The rules are simple enough to learn in one round:\n\n"
                "- Rows hold scrambled words.\n"
                "- Pick four words that belong together — a category, a synonym set, a themed group.\n"
                "- Place them in one row to complete the set.\n"
                "- Swap words between rows to shuffle the layout as you think.\n"
                "- Complete each group before the timer runs out.\n"
                "- Use a hint when a connection refuses to surface.\n\n"
                "There is no penalty for rearranging. Swapping is free, which is what makes the board "
                "feel like a worksheet you can scribble on rather than a locked puzzle. The clock is "
                "the only resource that actually costs you something."
            ),
        },
        {
            "h2": "How Do You Spot a Word Group?",
            "body": (
                "Grouping games reward a specific kind of looking. Instead of reading each word for "
                "meaning, scan for the relationship that could link four of them. The common group "
                "types are worth memorising:\n\n"
                "- Synonyms. Four words that mean roughly the same thing, often with different "
                "registers or intensities.\n"
                "- Category members. Four things that belong to one class — animals, tools, "
                "instruments, foods.\n"
                "- Shared wordplay. Words that take the same prefix or suffix, or hide a smaller word "
                "inside them.\n"
                "- Themed sets. Four words tied to one place, event or activity.\n\n"
                "The reliable technique is to sort the odd ones out first. If three words clearly "
                "belong to one theme and a fourth does not, that fourth is evidence about a different "
                "group. Eliminating impossible combinations narrows the board faster than staring at "
                "the most obvious candidate."
            ),
        },
        {
            "h2": "When Should You Use a Hint?",
            "body": (
                "Hints are a limited resource in most versions of this genre, and Unite Words uses "
                "them to highlight one valid group. The judgement call is simple:\n\n"
                "- Use a hint when you have a partial group. If you have three words that feel related "
                "and cannot find the fourth, the hint confirms the connection you already suspected "
                "and saves a full scan.\n"
                "- Do not burn a hint on a blank board. If nothing at all is connecting, a hint tells "
                "you one answer but teaches you nothing about the remaining groups.\n"
                "- Use the last hint when the timer is the real threat. Losing a board to a clock you "
                "could have beaten with one hint is the worst outcome in the game.\n\n"
                "Because completed special sets reveal new words, an early hint can also unlock "
                "content rather than just saving time — worth considering when you are close to a "
                "special set."
            ),
        },
        {
            "h2": "How Does Unite Words Compare to Other Word-Grouping Games?",
            "body": (
                "| Feature | Unite Words | Connections-style puzzles |\n"
                "| --- | --- | --- |\n"
                "| Board layout | Words arranged in rows | Words in a fixed grid |\n"
                "| Solving action | Line four words up in one row | Select four words at once |\n"
                "| Rearranging | Swap words between rows | No rearrangement |\n"
                "| New content | Special sets reveal new words | Groups revealed in place |\n"
                "| Pressure | Timer on the whole board | Limited mistakes per board |\n\n"
                "The row layout is the meaningful difference. Swapping gives you a physical way to "
                "test hypotheses, so the game plays more like sorting a hand of cards than answering "
                "a quiz. If you prefer a strict one-shot guess format, classic Connections rules will "
                "feel tighter; if you like thinking with your hands, the swapping is the appeal."
            ),
        },
        {
            "h2": "Is Unite Words Good for Learning English?",
            "body": (
                "It is a reasonable vocabulary workout, with an honest caveat. The game is entirely "
                "about recognising that words are related, which means it exercises exactly the skill "
                "language learners need: seeing categories and associations rather than translating "
                "word by word.\n\n"
                "What it does not do is teach meaning. If you do not know a word at all, grouping will "
                "not explain it — you will only infer it from its neighbours. That makes it useful "
                "for intermediate learners consolidating vocabulary, and less useful for beginners "
                "building it from scratch.\n\n"
                "The themed and synonym sets are the most instructive, because they force you to "
                "notice shades of meaning. The wordplay sets are the least instructive for "
                "learners, since they depend on spelling and affixes rather than usage."
            ),
        },
        {
            "h2": "Does Unite Words Work on Mobile?",
            "body": (
                "Yes. The game supports mouse, touchpad and touch input, so words can be selected and "
                "swapped on a phone or tablet without a keyboard. The row layout adapts to a narrow "
                "screen more naturally than a large grid, which makes it one of the better "
                "word-puzzle formats for mobile play.\n\n"
                "There is no account and no download — it runs in the browser through an embedded "
                "player. Progress is stored locally, so returning in the same browser usually keeps "
                "your place. Clearing browser data resets it."
            ),
        },
    ],
    "faq": [
        {"q": "Is Unite Words free to play?",
         "a": "Yes. It is free in the browser with no download and no account. The game is embedded "
              "directly on this page."},
        {"q": "How do you play Unite Words?",
         "a": "Find four related words and line them up in one row. Swap words between rows to "
              "rearrange the board, complete each set before the timer runs out, and use hints if you "
              "get stuck."},
        {"q": "What counts as a related group?",
         "a": "Groups can be synonyms, members of one category, words sharing a prefix or suffix, or "
              "words tied to one theme. The game does not label the type — recognising the connection "
              "is the puzzle."},
        {"q": "Are there hints in Unite Words?",
         "a": "Yes. A hint highlights one valid group of words so you can keep going when a "
              "connection refuses to surface."},
        {"q": "Does Unite Words have a timer?",
         "a": "Yes. Each board runs against a clock, so the game mixes word recognition with light "
              "time pressure."},
        {"q": "Is Unite Words good for learning English?",
         "a": "It trains category and association skills, which suits intermediate learners "
              "consolidating vocabulary. It does not explain unknown words, so beginners get less "
              "from it."},
        {"q": "Does it work on phones and tablets?",
         "a": "Yes. Touch input is supported, and the row layout fits a narrow screen well. No "
              "keyboard is required."},
        {"q": "Will my progress be saved?",
         "a": "Progress is stored locally in your browser because there is no account system. "
              "Returning in the same browser usually keeps your place; clearing site data resets it."},
    ],
}


PATCHES = {
    "maze-bomber": MAZE_BOMBER,
    "chips-bakery-simulator": CHIPS_BAKERY,
    "demolition-tycoon-3d": DEMOLITION,
    "unite-words": UNITE_WORDS,
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

    touched = []
    for g in data["games"]:
        patch = PATCHES.get(g["slug"])
        if not patch:
            continue
        g["description"] = patch["description"]
        g["sections"] = patch["sections"]
        g["faq"] = patch["faq"]
        g["date"] = "2026-11-10"
        wc = word_count(patch["sections"], patch["faq"])
        touched.append((g["slug"], wc))

    with open(DATA, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    for slug, wc in touched:
        print(f"[deepen] {slug:28} {wc} words")


if __name__ == "__main__":
    sys.exit(main())
