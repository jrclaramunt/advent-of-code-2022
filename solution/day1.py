from utils.base import Day


class Day1(Day):

    def __init__(self, args):
        self.calories_by_elf = Day1.calories_by_elf(args[0])

    def part1(self):
        return self.calories_by_elf[0]

    def part2(self):
        return sum(self.calories_by_elf[:3])

    @staticmethod
    def calories_by_elf(calories_by_snack):
        calories_count = 0
        calories_count_by_elf = []

        for i in list(calories_by_snack):
            try:
                calories_count += int(i.strip())
            except ValueError:
                calories_count_by_elf.append(calories_count)
                calories_count = 0

        calories_count_by_elf.append(calories_count)
        calories_count_by_elf.sort(reverse=True)

        return calories_count_by_elf

