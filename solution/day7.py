import re
from pprint import pprint

from utils.base import Day


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)

    def __repr__(self):
        return self.name


class Directory:
    def __init__(self, parent, name):
        self.content = []
        self.name = name
        self.parent = parent
        self.total_size = 0

    def add_file(self, file):
        self.content.append(file)

    def get_path(self):
        if self.parent is None:
            return '/'

        return self.parent_path(self.parent) + self.name + '/'

    def parent_path(self, directory):
        if directory is None:
            return ''
        if directory.parent is None:
            return '/'
        return self.parent_path(directory.parent) + directory.name + '/'

    def __repr__(self):
        return f'{self.name}: ' + ', '.join(map(lambda x: x.name, self.content))


class Day7(Day):

    def __init__(self, args):
        self.data_input = list(map(lambda x: x.strip(), args[0]))
        self.current_directory = None
        self.pointer = 0
        self.pointer = 0
        self.directories = {}

        while self.pointer < len(self.data_input):
            output_line = self.data_input[self.pointer]

            if output_line[0] == '$':
                self.eval_command(output_line)

    def part1(self):
        for directory in self.directories.values():
            directory.total_size = sum(x.size for x in directory.content)

        for directory in self.directories.values():
            self.total_size_dir(directory)

        return sum(x.total_size for x in self.directories.values() if x.total_size < 100000)

    def part2(self):
        pass

    def total_size_dir(self, directory):
        if directory.parent is None:
            return
        else:
            directory.parent.total_size += directory.total_size
            self.total_size_dir(directory.parent)

    def eval_command(self, command):
        if re.match(r'\$ cd (.+)', command) is not None:
            directory_name = re.match(r'\$ cd (.+)', command).groups()[0]
            if directory_name == '..':
                self.current_directory = self.directories[self.current_directory.get_path()].parent
            else:
                if self.current_directory is None:
                    new_directory = Directory(parent=self.current_directory, name=directory_name)
                    self.directories[new_directory.get_path()] = new_directory
                    self.current_directory = self.directories[new_directory.get_path()]
                else:
                    self.current_directory = self.directories[self.current_directory.get_path() + directory_name]

            self.pointer += 1

        elif re.match(r'\$ ls', command) is not None:
            self.pointer += 1

            try:
                while self.data_input[self.pointer][0] != '$':
                    line = self.data_input[self.pointer]

                    if re.match(r'dir (.+)', line):
                        directory_name = re.match(r'dir (.+)', line).groups()[0]

                        key = f'{self.current_directory.get_path()}{directory_name}/'

                        if self.directories.get(key) is None:
                            self.directories[key] = Directory(parent=self.current_directory, name=directory_name)

                    elif re.match(r'(\d+) (.+)', line) is not None:
                        file_info = re.match(r'(\d+) (.+)', line).groups()
                        new_file = File(size=file_info[0], name=file_info[1])

                        self.directories[self.current_directory.get_path()].add_file(new_file)

                    self.pointer += 1
            except IndexError:
                return
