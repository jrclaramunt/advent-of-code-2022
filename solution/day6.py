from utils.base import Day


class Day6(Day):

    def __init__(self, args):
        self.datastream_buffer = list(args[0][0])

    def part1(self):
        start_of_packet_position = 4
        return self.get_marker_position(start_of_packet_position)

    def part2(self):
        start_of_message_position = 14
        return self.get_marker_position(start_of_message_position)

    def get_marker_position(self, start):
        for i in range(len(self.datastream_buffer) - start):
            subsequence = self.datastream_buffer[i: i + start]
            if len(set(subsequence)) == start:
                return i + start
