from adventofcode2021.lib.advent_utils import DayTemplate


class Day(DayTemplate):
    def __init__(self):
        def a(s: str):
            d, n = s.split(" ")
            return (d, int(n))
        super().__init__(2, a)

    def part_1(self):
        super().part_1()

        depth = 0
        horiz = 0
        for direction, amount in self.data:
            if direction == "forward":
                horiz += amount
            elif direction == "up":
                depth -= amount
            elif direction == "down":
                depth += amount

        print(f"Depth: {depth}, Horiz {horiz}")
        return depth * horiz

    def part_2(self):
        super().part_2()

        depth = 0
        horiz = 0
        aim = 0

        for direction, amount in self.data:
            if direction == "forward":
                horiz += amount
                depth += (amount * aim)
            elif direction == "up":
                aim -= amount
            elif direction == "down":
                aim += amount

        print(f"Depth: {depth}, Horiz {horiz}")
        return depth * horiz
