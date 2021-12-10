from adventofcode2021.lib.advent_utils import DayTemplate


class Day(DayTemplate):
    def __init__(self):
        super().__init__(1, int)

    def part_1(self):
        super().part_1()

        last_measurement = None
        increases = 0
        for measurement in self.data:
            # There is no measurement before the first.
            if last_measurement is None:
                last_measurement = measurement
                continue

            if measurement > last_measurement:
                increases += 1

            last_measurement = measurement

        return increases

    def part_2(self):
        super().part_2()

        window = [None, None, None]
        increases = 0
        for measurement in self.data:
            last_window = window.copy()

            # Move the tape along
            window[2] = window[1]
            window[1] = window[0]
            window[0] = measurement

            if None in last_window:
                continue

            if sum(window) > sum(last_window):
                increases += 1

        return increases
