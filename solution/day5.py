import re
from collections import defaultdict

from utils.base import Day


class Crate:
    def __init__(self):
        self.supplies = []

    def push(self, element):
        self.supplies.append(element)

    def pop(self):
        try:
            return self.supplies.pop(-1)
        except IndexError:
            print(f"Stack is already empty")

    def add(self, supply):
        self.supplies.insert(0, list(supply)[1])


class Day5(Day):

    def __init__(self, args):
        self.input = list(map(lambda x: x, args[0]))

        for i in self.input:
            if re.match(r'( ?\d  ?)', i):
                break

        movements_line = self.init_cranes()
        self.supply_movement = self.input[movements_line:]

    def part1(self):
        action_regex = r'move (\d+) from (\d+) to (\d+)'
        for i in range(len(self.supply_movement)):
            data = re.match(action_regex, self.supply_movement[i].strip()).groups()

            units_to_move = int(data[0])
            origin = int(data[1])
            destination = int(data[2])

            for i in range(units_to_move):
                supply = self.crates[origin].pop()
                self.crates[destination].push(supply)

        result = ''
        for i in range(len(self.crates)):
            result += self.crates[i+1].pop()

        return result

    def part2(self):
        self.init_cranes()
        action_regex = r'move (\d+) from (\d+) to (\d+)'
        for i in range(len(self.supply_movement)):
            data = re.match(action_regex, self.supply_movement[i].strip()).groups()

            units_to_move = int(data[0])
            origin = int(data[1])
            destination = int(data[2])

            batch = []
            for j in range(units_to_move):
                supply = self.crates[origin].pop()
                batch.append(supply)

            batch.reverse()
            for j in batch:
                self.crates[destination].push(j)

        result = ''
        for i in range(len(self.crates)):
            result += self.crates[i + 1].pop()

        return result

    def init_cranes(self):
        regex_supplies = r'(   |\[[A-Z]\] ?|\\n)'
        self.crates = defaultdict(lambda: Crate())
        movements_line = 0
        for i in self.input:
            if re.match(r'( ?\d  ?)', i):
                break

            data = re.findall(regex_supplies, i)
            for i in range(len(data)):
                if data[i].strip() != '':
                    self.crates[i + 1].add(data[i].strip())

            movements_line += 1
        return movements_line + 2
