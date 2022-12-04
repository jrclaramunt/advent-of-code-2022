import re

from utils.base import Day


class Section:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_range(self):
        return range(self.start, self.end + 1)


class Day4(Day):

    def __init__(self, args):
        assignments = list(map(lambda x: x.strip(), args[0]))
        regex = r'(\d+)-(\d+),(\d+)-(\d+)'
        self.elves_sections = []

        for sections in assignments:
            sections_data = re.match(regex, sections).groups()
            elf_1_section = Section(int(sections_data[0]), int(sections_data[1]))
            elf_2_section = Section(int(sections_data[2]), int(sections_data[3]))
            self.elves_sections.append((elf_1_section, elf_2_section))

    def part1(self):
        ranges_contained = 0

        for section in self.elves_sections:
            elf_1_section = section[0].get_range()
            elf_2_section = section[1].get_range()

            if (section[0].start in elf_2_section and section[0].end in elf_2_section) or\
                    (section[1].start in elf_1_section and section[1].end in elf_1_section):
                ranges_contained += 1

        return ranges_contained

    def part2(self):
        overlaps = 0
        for section in self.elves_sections:
            elf_1_section = section[0].get_range()
            elf_2_section = section[1].get_range()

            if len(list(set(elf_1_section) & set(elf_2_section))) > 0:
                overlaps += 1

        return overlaps
