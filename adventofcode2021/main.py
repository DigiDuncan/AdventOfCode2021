import importlib
import pkgutil
import re

import adventofcode2021.days as day_modules
from adventofcode2021.lib.advent_utils import DayTemplate

days: dict[int, DayTemplate] = {}


def load_days():
    # https://stackoverflow.com/a/1708706
    daynames = [name for _, name, _ in pkgutil.walk_packages(day_modules.__path__, prefix = "adventofcode2021.days.")]
    for m in daynames:
        index = re.search(R"day(\d+)", m)
        if index is None:
            continue
        index = int(index.group(1))
        module = importlib.import_module(m)
        days[index] = module.Day()


def main():
    load_days()

    i = int(input("Input a day: "))
    if i not in days:
        print("Invalid day.")
    else:
        print(days[i])


if __name__ == "__main__":
    main()
