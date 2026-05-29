# Poco Loco Dice Game

A simple terminal-based dice game written in Python where players compete to lose all their chips first. Play against three AI opponents in a game of luck, strategy, and risky rerolls.

---

## Features

- ASCII-art dice display
- Turn-based gameplay
- Randomized player order each round
- AI opponents with simple decision-making
- Multiple scoring combinations:
  - **Poco!** → `4, 5, 6`
  - **Loco!** → `1, 2, 3`
  - Three-of-a-kind
  - Standard point scoring
- Chip tracking system
- Tie-breaker handling

---

## How to Run

Make sure Python 3 is installed on your computer.

Run the game in your terminal:

```bash
python PocoLoco.py
```

---

## Game Rules

### Objective

Be the first player to lose all your chips.

### Gameplay

1. Each player rolls 3 dice.
2. The first player may roll up to 3 times.
3. Other players may roll up to the same number of rolls as the player before them.
4. Players can choose to reroll and try for a better score.

### Scoring

| Combination | Result |
|---|---|
| `4,5,6` | Poco! |
| `1,2,3` | Loco! |
| Three of a kind | High score |
| Other rolls | Point-based scoring |

### Chips

- The lowest-scoring player receives chips based on the winner’s roll strength.
- The game continues until a player reaches 0 chips.

---

## Author

Created by Damiano Racic.
