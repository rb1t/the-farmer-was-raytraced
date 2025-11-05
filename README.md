# The Farmer Was Raytraced (Replaced)

Really just for personal use, having fun playing this game and learning more coding :)

## File Overview

### Core files

- `cell.py` is a single block in the world map. This is used to index and store each cell's properties (e.g., its id, if it was Fertilized, what is planted on it, etc.). 
- `drone` a helper to track and inter each done, just like each cell
- `do.py` a library of common functions
- `static.py` stores global/common unchanging variables, or at least those that don't change after being initialized. E.g., the world size, the items and entities that exist, and compass directions).
- `database.py` global/common variables that do change. E.g., the state of a cell, or the locations of walls in mazes.
- `maze.py` has some functions specific to building and solving mazes
- `main.py` and `main2.py` where I'm running my main game from (really only need one of these)

### Other files

- `achievements.py` had the idea to put all achievements in one spot .. needs a lot of work!
- `do_harvest_basic.py` SUPER basic. I wanted to keep something from my earliest beginings in this game. A time when I was just getting familiar with the mechanics, and back into more coding. I deleted, cleaned, or refactored everything else :(
- `clear.py` if they implement a way to assign a 'main' Module/window, they could have a Play and Clear button in the GUI. Until then, sometimes I just wanna press clear ...
- `NOTES.md` Just some personal stuff I still wanna do - or do more of - in the game.
- `README.md` This file :3
- `.gitignore` Mostly just to ignore some Game [and Kate] project files.
