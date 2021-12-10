from adventofcode2021.lib.advent_utils import DayTemplate, ThisShouldNeverHappenExeception


class Day(DayTemplate):
    def __init__(self):
        super().__init__(3)

    def part_1(self):
        super().part_1()

        zero_counts = [0] * 12
        one_counts = [0] * 12
        # Get the values we need
        for s in self.data:
            for i in range(12):
                if s[i] == "0":
                    zero_counts[i] += 1
                elif s[i] == "1":
                    one_counts[i] += 1
                else:
                    raise ThisShouldNeverHappenExeception

        gamma_list = [0 if zero_counts[i] > one_counts[i] else 1 for i in range(12)]
        epsilon_list = [0 if i == 1 else 1 for i in gamma_list]
        gamma_string = "".join([str(i) for i in gamma_list])
        epsilon_string = "".join([str(i) for i in epsilon_list])
        gamma = int(gamma_string, 2)
        epsilon = int(epsilon_string, 2)

        print(f"γ: {gamma_string} | {gamma}")
        print(f"ε: {epsilon_string} | {epsilon}")
        return gamma * epsilon

    def part_2(self):
        super().part_2()
