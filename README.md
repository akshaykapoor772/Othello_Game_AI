# Othello/Reversi AI Game

## Overview
This project implements the classic board game Othello (also known as Reversi) with multiple AI agents. Players can choose between various agents or even play themselves.

Agents:
1. __Human Player:__ 
* A human user can play the game through command-line prompts.

2. __Random Agent:__
* Chooses moves randomly from the available legal moves.
* Has a 50% chance of winning.
* Average move time: 0.0281 seconds.

3. __Minimax Agent:__
* Uses the minimax algorithm to select the optimal move.
* Accepts a depth parameter to determine how many moves ahead it should consider.
* Move times vary based on depth. (e.g., Depth 2: 2.7940 seconds, Depth 3: 24.50 seconds.)

4. __Alphabeta Agent:__
* Implements the minimax algorithm with alpha-beta pruning.
* Optimized with alpha-beta pruning for faster results and deeper searches.
* Winning chances increase with greater search depth.

## Requirements
* Python 3

## How to Run
Execute the run.sh script with one to three arguments:

```bash
./run.sh [agent1] [agent2] [depth_or_time]
```
* [agent1]: Specifies the player/agent for Player 1. Choices include human, random, minimax, alphabeta, and possibly others.
* [agent2]: Specifies the player/agent for Player 2.
* [depth_or_time]: (Optional) Depth or time parameter for agents that require it.

Examples:
To have a human play against a random agent:
```bash
./run.sh human random
```
To have two alphabeta agents play against each other with a search depth of 3:

```bash
./run.sh alphabeta alphabeta 3
```

## Game Logic and Implementation
The game logic, board state, and game progression are managed in othello.py and game.py. The different agent strategies are implemented in agent.py.

## Sample Runs
For examples of the game being executed with different agents and configurations, please refer to SampleRun.pdf.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
