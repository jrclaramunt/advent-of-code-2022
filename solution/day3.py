from enum import Enum

from utils.base import Day


class Day3(Day):

    def __init__(self, args):
        self.rucksacks = list(map(lambda x: x.strip(), args[0]))

    def part1(self):
        total_priority = 0

        for rucksack in self.rucksacks:
            compartiment_1 = rucksack[0:int(len(rucksack)/2)]
            compartiment_2 = rucksack[int(len(rucksack)/2):]
            common_items = list(set(compartiment_1) & set(compartiment_2))
            total_priority += Day3.get_priority(common_items[0])

        return total_priority

    def part2(self):
        total_priority = 0
        elves_by_group = 3

        for i in range(0, len(self.rucksacks), elves_by_group):
            common_items = list(set(self.rucksacks[i]) & set(self.rucksacks[i + 1]) & set(self.rucksacks[i + 2]))
            total_priority += Day3.get_priority(common_items[0])

        return total_priority

    @staticmethod
    def get_priority(item):
        lowercase_letter_items_first_priority = 1
        uppercase_letter_items_first_priority = 27

        if 'a' <= item <= 'z':
            return ord(item) - ord('a') + lowercase_letter_items_first_priority
        else:
            return ord(item) - ord('A') + uppercase_letter_items_first_priority
