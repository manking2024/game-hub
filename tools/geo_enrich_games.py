#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GEO bulk enrichment for puzzle + arcade games.
Appends one question-style section and three real FAQ entries per game.
All content is derived from each game's existing official description
(summary/description) — no invented numbers. Run once, then regenerate site.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "games.json")

PROGRESS_FAQ = ("Will my progress save?", "Since there is no account, progress is stored locally in your browser. Closing the tab and coming back usually keeps your place; clearing browser data resets it.")

def age_faq(slug, note=""):
    return ("Is {} suitable for kids?".format(slug_title(slug)),
            "Based on its content it is a family-friendly pick for most ages{}. Parental oversight is always a good idea for younger players.".format(" " + note if note else ""))

def slug_title(slug):
    return slug.replace("-", " ").title()

EXTRAS = {
  "crash-tower-3d": {
    "sec": ("What is the best way to clear all 30 stages?",
            "Crash Tower 3D is a physics destruction run: launch your vehicle, hit the boost pad inside the gold zone, and smash through 30 progressively tougher towers. Coins you earn let you upgrade so later stages stay beatable. The trick is timing — hit the boost zone cleanly instead of grazing it."),
    "faqs": [
      ("How long does a run take?", "Each stage is a single smash, so a run is measured in seconds. 30 stages total gives you a satisfying loop without a big time commitment."),
      age_faq("crash-tower-3d", "it is cartoon-style vehicle destruction with no blood"),
      PROGRESS_FAQ,
    ],
  },
  "box-press-puzzle": {
    "sec": ("Why is press order more important than speed?",
            "Box Press Puzzle is a mechanical Sokoban-style brain teaser: fire pistons in the right order to push smooth cyan cubes into the central drop zone. Press too early and a cube can wedge against a wall or block another cube's path — restarting costs seconds, so plan the sequence before you start firing."),
    "faqs": [
      ("How is Box Press Puzzle different from classic Sokoban?", "Classic Sokoban uses a walking character; Box Press Puzzle replaces movement with piston presses. The puzzle logic is the same — order and access matter — but the interaction is cleaner and faster to reset."),
      age_faq("box-press-puzzle"),
      PROGRESS_FAQ,
    ],
  },
  "unite-words": {
    "sec": ("How do word sets work?",
            "Unite Words gives you a grid of tiles and asks you to find groups of four related words and line them up in one row. You swap words between rows and complete each set before the timer runs out. When you get stuck, the hint system nudges you toward the next connection."),
    "faqs": [
      ("Is Unite Words a good game for learning English?", "It is an English word puzzle — recognizing related words and categories is the whole game, so it doubles as a light vocabulary workout."),
      age_faq("unite-words", "it is a pure word game"),
      PROGRESS_FAQ,
    ],
  },
  "candy-shop-3d-match-puzzle": {
    "sec": ("How is this different from classic match-3?",
            "Candy Shop is a 3D candy puzzle: instead of swapping tiles on a flat board, you tap three matching candy pieces and clear them from a layered scene. The 3D view means depth matters — pieces behind others are harder to see and plan around."),
    "faqs": [
      ("How long does a level take?", "Levels are bite-sized — a couple of minutes each. The exact stage count depends on the current version, so check inside the game."),
      age_faq("candy-shop-3d-match-puzzle", "it is a colorful candy theme"),
      PROGRESS_FAQ,
    ],
  },
  "blasties": {
    "sec": ("What makes a good chain?",
            "Blasties is a candy-based shooter: fire candies from the ground and aim for chains of similar candies. Longer chains clear more of the board and set up bigger combos, so the fun is planning where each shot lands rather than firing randomly."),
    "faqs": [
      ("How long does a round take?", "Rounds are quick and restart instantly, which makes Blasties easy to pick up between tasks."),
      age_faq("blasties", "it is a colorful candy shooter with no violence"),
      PROGRESS_FAQ,
    ],
  },
  "marblemaze": {
    "sec": ("How do you survive the maze?",
            "MarbleMaze is a rolling-ball escape: guide a glossy marble to the green goal while dodging red hazards and decoy balls that look safe until they are not. Reading the board a few moves ahead is the core skill — the fast paths are usually the deadly ones."),
    "faqs": [
      ("Is MarbleMaze more about reflexes or planning?", "Both, but planning wins. The maze is fixed, so studying routes and decoys before rolling keeps runs alive much longer than twitch reactions alone."),
      age_faq("marblemaze", "it is a harmless maze-escape theme"),
      PROGRESS_FAQ,
    ],
  },
  "draw-the-railball-physics": {
    "sec": ("What tools can you draw?",
            "Draw the RailBall Physics lets you sketch rails and pipes to guide a rolling ball to the goal. Planks, springs, accelerators and bumpers each change the ball's momentum differently, so every level is a tiny physics experiment: build, test, adjust."),
    "faqs": [
      ("Is it a creativity game or a puzzle game?", "Both. The objective is fixed, but the path is open — different drawings solve the same level, which makes it more creative than a strict logic puzzle."),
      age_faq("draw-the-railball-physics", "it is a construction-style physics toy"),
      PROGRESS_FAQ,
    ],
  },
  "ricochet-paint-aim": {
    "sec": ("How do you plan a bounce?",
            "Ricochet Paint Aim is a peg-maze shooter: aim, calculate the bounce, and launch your ball through intricate peg fields to splatter the target zones. Walls and pegs deflect your shot, so reading the angles beats firing fast."),
    "faqs": [
      ("Does it require precise aim?", "Yes — angle reading is the core. The payoff is satisfying: one well-planned bounce can clear several targets at once."),
      age_faq("ricochet-paint-aim", "it is a paint-splat arcade theme"),
      PROGRESS_FAQ,
    ],
  },
  "wood-builder-tycoon": {
    "sec": ("What does the tycoon loop look like?",
            "Wood Builder Tycoon is a lumber empire builder: chop down massive trees, upgrade high-tech sawmills, and transport timber to grow your operation. Every upgrade shortens the chain from tree to cash, so the loop is chop, mill, ship, reinvest."),
    "faqs": [
      ("Is it an idle game or an active one?", "It sits between the two — income keeps flowing while you upgrade, but active play speeds progress noticeably."),
      age_faq("wood-builder-tycoon", "it is a clean business-building theme"),
      PROGRESS_FAQ,
    ],
  },
  "worm-path": {
    "sec": ("What makes Worm Path tricky?",
            "Worm Path is a logic maze: guide a clever worm through increasingly tricky grids to reach the exit. It looks like a snake game, but there is no speed pressure — the difficulty is pure spatial planning."),
    "faqs": [
      ("Is it like a snake game?", "Only in looks. There is no chase and no timer pressure — it is a turn-by-turn logic puzzle where route planning decides everything."),
      age_faq("worm-path", "it is a calm logic puzzle"),
      PROGRESS_FAQ,
    ],
  },
  "double-heist-rob-the-robbers": {
    "sec": ("How does a heist play out?",
            "Double Heist flips the story: the robbers already hit the bank, and your job is to rob the robbers. Crack their safes before they get away — each safe is a timed puzzle, and the getaway clock keeps the pressure on."),
    "faqs": [
      ("Is the heist theme violent?", "No — it is a cartoon caper about cracking safes, not a shooter. The tension comes from the timer, not from weapons."),
      age_faq("double-heist-rob-the-robbers"),
      PROGRESS_FAQ,
    ],
  },
  "yaoguard": {
    "sec": ("How does tower defense work here?",
            "YAOGUARD is a tower-defense game set in the mythic Shan Hai world: command legendary guardians and place them along enemy paths to stop the invasion. Each guardian brings a different attack pattern, so lane placement matters as much as the lineup."),
    "faqs": [
      ("Is it beginner-friendly tower defense?", "The guardian placement keeps the classic tower-defense loop simple to start, while later waves demand smarter positioning."),
      age_faq("yaoguard", "it is a fantasy defense theme with no gore"),
      PROGRESS_FAQ,
    ],
  },
  "museum-night-shift": {
    "sec": ("How does the turn-based guard work?",
            "Museum Night Shift is a turn-based puzzle: patrol the museum as a guard and out-think a cunning thief whose plans shift with every step you take. Each move changes the board, so you are really playing against the thief's future moves."),
    "faqs": [
      ("Is it a strategy game?", "Yes — it is turn-based planning, closer to chess than to action. Every patrol step rewrites the thief's options."),
      age_faq("museum-night-shift", "it is a clean security-puzzle theme"),
      PROGRESS_FAQ,
    ],
  },
  "spinwhisker": {
    "sec": ("How do you help the cat get home?",
            "SpinWhisker is a puzzle adventure about a lost cat who strayed too far from home. You solve environment puzzles to guide him back — spinning, moving and re-arranging objects to open a path."),
    "faqs": [
      ("Is it a story game?", "Lightly — the lost-cat setup gives the puzzles a goal beyond scoring, which keeps casual players engaged."),
      age_faq("spinwhisker", "it is a cute animal-theme puzzle"),
      PROGRESS_FAQ,
    ],
  },
  "ragdoll-teleport-arena": {
    "sec": ("How does the teleport shot work?",
            "Ragdoll Teleport Arena is an action-puzzler: shoot a projectile to hit enemies and deal damage, then tap again mid-flight to teleport your character to the projectile. Positioning and timing decide whether you land the hit or walk into the crossfire."),
    "faqs": [
      ("What is the core skill?", "Reading the arena and timing the second tap. The teleport is both your attack setup and your movement — the same button does double duty."),
      age_faq("ragdoll-teleport-arena", "it is cartoon ragdoll combat with no blood"),
      PROGRESS_FAQ,
    ],
  },
  "ragdoll-rush-3d-sky-race": {
    "sec": ("What is inside the 25 courses?",
            "Ragdoll Rush 3D: Sky Race sends you tumbling through 25 obstacle courses across five colorful worlds, racing two computer-controlled rivals. Each world adds a new kind of obstacle, and the ragdoll physics keep every fall funny rather than frustrating."),
    "faqs": [
      ("How many levels are there?", "25 courses across 5 worlds, per the official description — a solid single-sitting campaign with a race twist."),
      age_faq("ragdoll-rush-3d-sky-race", "it is slapstick ragdoll racing"),
      PROGRESS_FAQ,
    ],
  },
  "elemental-challenge": {
    "sec": ("How do you combine elements?",
            "Elemental Challenge is a logic game about combining elemental pieces into complete elements. Match the right pieces and they merge into something new; the chain of combinations is where the puzzle lives."),
    "faqs": [
      ("Is it a crafting or a logic game?", "Logic first — you already know the possible outcomes, and the puzzle is choosing the order that clears the board."),
      age_faq("elemental-challenge", "it is a clean element-theme puzzle"),
      PROGRESS_FAQ,
    ],
  },
  "tower-siege": {
    "sec": ("How does build-and-defend work?",
            "Tower Siege deals you a hand of four block shapes each wave: build your tower, then defend it. Between waves you place the shapes you drew, so the tower you get is the tower you planned around — shape luck is part of the strategy."),
    "faqs": [
      ("Is it more building or defending?", "Both share the same resource: your block hand. Good builders survive more waves, which is the whole loop."),
      age_faq("tower-siege", "it is a block-defense theme"),
      PROGRESS_FAQ,
    ],
  },
  "halloween-survivor": {
    "sec": ("How do the orbiting swords work?",
            "Halloween Survivor drops you into a spooky world where your swords orbit around you automatically. Survive endless waves of enemies by keeping distance and letting the orbit do the damage — movement, not aiming, is the skill."),
    "faqs": [
      ("How long does a run last?", "It is endless survival — runs last as long as you survive, so sessions can be as short as a minute or as long as you can hold out."),
      age_faq("halloween-survivor", "it is cartoon-style monster waves with no gore"),
      PROGRESS_FAQ,
    ],
  },
  "slime-buffet": {
    "sec": ("What are the 100 mosaic levels like?",
            "Slime Buffet is a color-puzzle feast: guide a crowd of hungry slimes through 100 candy-mosaic levels. Every level is a small color-matching riddle, and the mosaic art is what keeps the hundred stages from feeling repetitive."),
    "faqs": [
      ("How many levels are there?", "100 candy-mosaic levels, per the official description — a long, structured campaign for puzzle fans."),
      age_faq("slime-buffet", "it is a cheerful candy/slime theme"),
      PROGRESS_FAQ,
    ],
  },
  "maze-evolution-html": {
    "sec": ("What is Maze Evolution?",
            "Maze Evolution HTML is a browser recreation of the classic Flash puzzle Maze Evolution. You guide the snake through evolving mazes, keeping the old-school challenge alive without needing Flash."),
    "faqs": [
      ("Do I need Flash to play?", "No — this is an HTML5 recreation, so it runs directly in a modern browser."),
      age_faq("maze-evolution-html", "it is a calm maze puzzle"),
      PROGRESS_FAQ,
    ],
  },
  "snake-way": {
    "sec": ("How do snakes find their path?",
            "Snake Way is a colorful logic maze: guide each snake through clever paths and help them reach their destinations. Routes overlap, so ordering your moves is the real puzzle — which snake goes first changes everything."),
    "faqs": [
      ("Is it a fast snake game?", "No — it is a calm route-planning puzzle. The challenge is sequence, not speed."),
      age_faq("snake-way", "it is a friendly color-theme puzzle"),
      PROGRESS_FAQ,
    ],
  },
  "break-a-lucky-egg-brainrots": {
    "sec": ("What is the risk-reward loop?",
            "Break a Lucky Egg Brainrots is a fast collection game where action, risk and strategy meet: break eggs, grab rewards, and decide when to push for a bigger payout and when to bank what you have."),
    "faqs": [
      ("Is it a clicker or a strategy game?", "A mix — collecting is quick, but knowing when to stop and cash out is the strategic layer."),
      age_faq("break-a-lucky-egg-brainrots", "it is a cartoon egg-collection theme"),
      PROGRESS_FAQ,
    ],
  },
  "town-builder-inc": {
    "sec": ("How do you grow the town?",
            "Town Builder Inc. is a cash-stacking tycoon: collect cash, stack your earnings, and unlock town businesses one by one. Upgrading capacity and hiring workers compounds the income, turning a single shop into a full town."),
    "faqs": [
      ("Is it an idle tycoon?", "Mostly — money keeps ticking while you upgrade, and each unlock gives the town a visible new building."),
      age_faq("town-builder-inc", "it is a clean business-building theme"),
      PROGRESS_FAQ,
    ],
  },
  "ants-clear-all-color-block-puzzle": {
    "sec": ("How do the ants clear blocks?",
            "Ants Clear All is a single-player color-block puzzle: send out your ants and carry every colorful block away. Matching colors and planning the order ants move keeps the clearing efficient — the goal is a completely empty board."),
    "faqs": [
      ("Is it a memory or logic game?", "Logic — reading which blocks can be cleared next and planning the order is the whole puzzle."),
      age_faq("ants-clear-all-color-block-puzzle", "it is a colorful ant-theme puzzle"),
      PROGRESS_FAQ,
    ],
  },
  "geometry-vibes": {
    "sec": ("What is the core challenge?",
            "Geometry Vibes is the reaction-based original: avoid obstacles, traps and spikes that rush at you in rhythm. The X-Ball edition builds on this core with new levels, a challenge section and a rebuilt store — if you like one, the other extends it."),
    "faqs": [
      ("How is it different from Geometry Vibes X Ball?", "This is the original reaction run; X-Ball adds new levels, a challenge mode and a rebuilt store on top of the same one-button core."),
      age_faq("geometry-vibes", "it is a neon rhythm-avoidance game"),
      PROGRESS_FAQ,
    ],
  },
  "snake-block-rush": {
    "sec": ("How does the rush work?",
            "Snake Block Rush is a hyper-casual arcade take on snake: guide a neon bead snake, collect white bonus orbs to grow, and keep the chain moving. Rounds are fast and one-more-go friendly."),
    "faqs": [
      ("How long does a round take?", "A couple of minutes — the design is built for quick sessions and instant restarts."),
      age_faq("snake-block-rush", "it is a neon arcade classic"),
      PROGRESS_FAQ,
    ],
  },
  "snow-rush-3d": {
    "sec": ("How do you ride the sled?",
            "Snow Rush 3D is a winter sledding race that tests speed and reflexes: steer down snowy slopes, dodge obstacles, and chase the fastest line. It is built for short, thrilling runs in the browser."),
    "faqs": [
      ("Is it easy to pick up?", "Yes — steering and dodging is the whole control set, so the first run works immediately and the skill curve is about choosing lines."),
      age_faq("snow-rush-3d", "it is a family-friendly winter theme"),
      PROGRESS_FAQ,
    ],
  },
}


def main():
    with open(DATA, "r", encoding="utf-8-sig") as f:
        data = json.load(f)

    applied = 0
    for g in data["games"]:
        slug = g["slug"]
        if slug not in EXTRAS:
            continue
        extra = EXTRAS[slug]
        h2, body = extra["sec"]
        g.setdefault("sections", []).append({"h2": h2, "body": body})
        g.setdefault("faq", []).extend(
            {"q": q, "a": a} for q, a in extra["faqs"]
        )
        applied += 1

    with open(DATA, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"[enrich] applied extras to {applied} games -> {DATA}")


if __name__ == "__main__":
    main()
