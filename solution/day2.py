from enum import Enum

from utils.base import Day


class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcome(Enum):
    WIN = 1,
    LOSE = 2,
    DRAW = 3


class Day2(Day):

    def __init__(self, args):
        self.strategy_guide = list(map(lambda x: x, args[0]))
        self.rival_moves = {
            'A': Move.ROCK,
            'B': Move.PAPER,
            'C': Move.SCISSORS
        }

    def part1(self):
        player_moves = {
            'X': Move.ROCK,
            'Y': Move.PAPER,
            'Z': Move.SCISSORS
        }
        count = 0

        for entry in self.strategy_guide:
            player_move = (entry.split(' ')[1]).strip()
            rival_move = entry.split(' ')[0]
            count += Day2.get_player_score(player_moves[player_move], self.rival_moves[rival_move])

        return count

    def part2(self):
        outcome = {
            'X': Outcome.LOSE,
            'Y': Outcome.DRAW,
            'Z': Outcome.WIN
        }
        count = 0

        for entry in self.strategy_guide:
            desired_outcome = (entry.split(' ')[1]).strip()
            rival_move = entry.split(' ')[0]
            player_move = Day2.calculate_player_move(self.rival_moves[rival_move], outcome[desired_outcome])
            count += Day2.get_player_score(player_move, self.rival_moves[rival_move])

        return count

    @staticmethod
    def get_player_score(player_move, rival_move):
        if player_move.value == rival_move.value:
            return 3 + player_move.value
        elif player_move.value == rival_move.value % 3 + 1:
            return 6 + player_move.value
        else:
            return 0 + player_move.value

    @staticmethod
    def calculate_player_move(rival_move, outcome):
        if outcome == Outcome.DRAW:
            return rival_move
        elif outcome == Outcome.WIN:
            winning_move = rival_move.value % 3 + 1
            return Move(winning_move)
        else:
            losing_move = (rival_move.value % 3 - 2) % 3 + 1
            return Move(losing_move)



