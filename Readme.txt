# Stone Paper Scissors 🪨📄✂️

A simple command-line Stone Paper Scissors game written in Python.

## How to Run

Make sure you have Python installed, then run:

```bash
python sps.py
```

## How to Play

When prompted, type your choice:

```
enter your choice: stone
```

Accepted inputs: `stone`, `paper`, `scissors` all lowercase.

The computer picks randomly, and the result is displayed instantly.

## Example

```
enter your choice stone
computer plays Paper and you plays stone
you lose
```

## How the Logic Works

Instead of writing all 6 win/lose conditions separately, the game uses a neat math trick with the difference between the computer's and player's choices (mapped to 1, 2, 3):

| Difference | Result     |
|------------|------------|
| 0          | Draw       |
| -1 or +2   | You win    |
| anything else | You lose |