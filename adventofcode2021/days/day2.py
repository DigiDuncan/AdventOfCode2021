from adventofcode2021.lib.advent_utils import DayTemplate


class Day(DayTemplate):
    def __init__(self):
        super().__init__(2, lambda s: [(x, int(y)) for x, y in s.split(" ")])

    def part_1(self):
        for direction, amount in self.data:
            pass
        return 0

    def part_2(self):
        return 0
