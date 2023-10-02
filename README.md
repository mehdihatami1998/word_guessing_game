# Word Guesser Game
## Introduction
This is a game in which the computer randomly chooses a word from different categories, and the user has to guess it. The user can guess the word by guessing the letters in the word. The user has as many chances as the number of letters in the word. The user can also ask for a hint, which will reveal a letter in the word. If the user can guess the word correctly, the user wins, otherwise the user loses.
## Pre-requisit
This game doesn't need any special pre-requisit. It only needs a python interpreter to run.

## Directory Structure
```
word_guesser_game
|-- src/
|  |-- main.py
|  |-- utils/
|  |  |-- word_generator.py
|  |  |-- hint_generator.py
|  |  |-- input_validator.py
|  |-- game_logic/
|-- README.md
|-- requirements.txt
```

## How to Run
1. Navidate to the root directory of the project (WORD_GUESSER_GAME).
2. Add current directory to the python path.
    ```
    export PYTHONPATH="${PYTHONPATH}:$(pwd)"
    ```
3. Run the game
    ```
    python main.py
    ```
4. Follow on-screen prompts to play the game.
## Modules

- `src/utils/`: This directory contains the utility modules used in the game.  
    - `src/utils/word_generator.py`: This module is used to generate random words from different categories.  
    - `src/utils/hint_generator.py`: This module is used to generate hints for the user.

    - `src/utils/input_validator.py`: This module is used to validate the user input.
- `src/game_logic/`: This directory contains the game logic modules.
- `src/main.py`: This is the main module of the game. It contains the main function which is the entry point of the game.
#test