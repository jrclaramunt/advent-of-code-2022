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
        data_input = list(map(lambda x: x, args[0]))
        movements_line = self.get_movements_index(data_input)

        self.crates_initial_state = data_input[:movements_line - 2]
        self.supply_movement = data_input[movements_line:]
        self.action_regex = r'move (\d+) from (\d+) to (\d+)'

    def part1(self):
        crates = self.init_cranes()

        for i in range(len(self.supply_movement)):
            data = re.match(self.action_regex, self.supply_movement[i].strip()).groups()

            units_to_move = int(data[0])
            origin = int(data[1])
            destination = int(data[2])

            for _ in range(units_to_move):
                supply = crates[origin].pop()
                crates[destination].push(supply)

        return self.get_cranes_top(crates)

    def part2(self):
        crates = self.init_cranes()
        action_regex = r'move (\d+) from (\d+) to (\d+)'
        for i in range(len(self.supply_movement)):
            data = re.match(action_regex, self.supply_movement[i].strip()).groups()

            units_to_move = int(data[0])
            origin = int(data[1])
            destination = int(data[2])

            batch = []
            for _ in range(units_to_move):
                supply = crates[origin].pop()
                batch.append(supply)

            batch.reverse()
            for j in batch:
                crates[destination].push(j)

        return self.get_cranes_top(crates)

    def init_cranes(self):
        regex_supplies = r'(   |\[[A-Z]\] ?|\\n)'
        crates = defaultdict(lambda: Crate())

        for i in self.crates_initial_state:
            data = re.findall(regex_supplies, i)
            for i in range(len(data)):
                if data[i].strip() != '':
                    crates[i + 1].add(data[i].strip())

        return crates

    @staticmethod
    def get_cranes_top(crates):
        return ''.join(map(lambda x: crates[x + 1].pop(), range(len(crates))))

    @staticmethod
    def get_movements_index(input_data):
        for i in range(len(input_data)):
            if re.match(r'( ?\d  ?)', input_data[i]):
                return i + 2
