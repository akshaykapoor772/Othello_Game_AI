import random
import time

import game

class HumanPlayer(game.Player):

    def __init__(self):
        super().__init__()

    def choose_move(self, state):
        # generate the list of moves:
        moves = state.generateMoves()

        for i, action in enumerate(moves):
            print('{}: {}'.format(i, action))
        response = input('Please choose a move: ')
        return moves[int(response)]


class RandomAgent(game.Player):

    def __init__(self):
        super().__init__()

    def choose_move(self, state):
        moves = state.generateMoves()
        list = []

        for i, action in enumerate(moves):
            print('{}: {}'.format(i, action))
            list.append(i)
        if len(list):
            response = random.choice(list)
            return moves[int(response)]
        else:
            pass


class MinimaxAgent(game.Player):

    def __init__(self, depth):
        super().__init__()
        self.depth = depth


    def choose_move(self, state):
        moves = state.generateMoves()
        bestVal = -1000
        bestMove = None

        for i, action in enumerate(moves):
            print('{}: {}'.format(i, action))

        if len(moves):
            for move in moves:
                newstate = state.applyMoveCloning(move)
                moveVal = self.minimax(newstate, False, 0)
                if (moveVal > bestVal):
                    bestMove = move
                    bestVal = moveVal
            return bestMove

        else:
            pass

    def minimax(self,state, isMax, depth):
        if depth <= self.depth:

            moves = state.generateMoves()
            if isMax:
                bestVal = -1000
                for move in moves:
                    value = self.minimax(state, False, depth+1)
                    bestVal = max(bestVal, value)
                return bestVal

            else:
                bestVal = 1000
                for move in moves:
                    value = self.minimax(state, True, depth+1)
                    bestVal= min(bestVal, value)
                return bestVal
        else:
            return state.score()




class AlphaBeta(game.Player):
    def __init__(self, depth):
        super().__init__()
        self.depth = depth

    def choose_move(self, state):
        moves = state.generateMoves()
        bestVal = -1000
        bestMove = None
        alpha = 1000
        beta = -1000

        for i, action in enumerate(moves):
            print('{}: {}'.format(i, action))

        if len(moves):
            for move in moves:
                newstate = state.applyMoveCloning(move)
                moveVal = self.minimax(newstate, False, 0, alpha, beta)
                if (moveVal > bestVal):
                    bestMove = move
                    bestVal = moveVal
            return bestMove

        else:
            pass

    def minimax(self, state, isMax, depth, alpha, beta):
        if depth <= self.depth:

            moves = state.generateMoves()
            if isMax:
                bestVal = -1000
                for move in moves:
                    value = self.minimax(state, False, depth + 1, alpha, beta)
                    bestVal = max(bestVal, value)
                    alpha = max(alpha, bestVal)
                    if beta <= alpha:
                        break
                return bestVal

            else:
                bestVal = 1000
                for move in moves:
                    value = self.minimax(state, True, depth + 1, alpha, beta)
                    bestVal = min(bestVal, value)
                    beta = min(beta, bestVal)
                    if beta <= alpha:
                        break
                return bestVal
        else:
            return state.score()

