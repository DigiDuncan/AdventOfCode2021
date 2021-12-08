# Advent Of Code 2021
My solutions to the [Advent of Code 2021](https://adventofcode.com/2021) challenge.

## To get this working:
* `cd` into the root directory and run `pip install .`, or set up your Python enviroment however you want. Make sure you're using 3.9+.
* Place the value of your `session` cookie from http://adventofcode.com in a file called `cookie.txt` in the `adventofcode2021/data` directory. (You can get this using a browser add-on like [Cookie Quick Manager](https://github.com/ysard/cookie-quick-manager) for Firefox.)
* Run `python -m adventofcode2021`.
* Input the day you'd like to see the answer for.

All the day's solutions are stored in files called `adventofcode2021/days/day`N`.py`, N being the day number. Each day has a `.data` property which is a list of the cleaned data that is looped over to find the solution. The template used for these days can be found in `adventofcode/lib/advent_utils` as `DayTemplate`.
