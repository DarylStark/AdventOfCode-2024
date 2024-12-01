"""Solutions for Advent of Code 2024 - Day 1."""

from aoc import DaySolution


class Day01(DaySolution):
    """Solution for Day 01.

    Link: https://adventofcode.com/2024/day/1

    Needed for this solution:
    -   A `input` file from the Advent of Code website. This can be found at
        the link above. Give the location of this file in the `input_file`
        argument of the constructor for the object.
    """

    def __init__(self, input_file: str) -> None:
        """Set internal values."""
        self._input_file = input_file
        self._loaded_data = False
        self._list_a: list[int] = []
        self._list_b: list[int] = []

    def _load_data(self) -> None:
        """Load data from the input file."""
        if self._loaded_data:
            return

        with open(self._input_file, encoding='utf-8') as file:
            for line in file:
                splitted = line.strip().split()
                self._list_a.append(int(splitted[0]))
                self._list_b.append(int(splitted[1]))
        self._loaded_data = True

    def solve_puzzle_one(self) -> str:
        """Solve puzzle one."""
        self._load_data()
        self._list_a.sort()
        self._list_b.sort()

        distance: int = 0
        for item in enumerate(self._list_a):
            items = [item[1], self._list_b[item[0]]]
            distance += max(items) - min(items)

        return str(distance)

    def solve_puzzle_two(self) -> str:
        """Solve puzzle two."""
        self._load_data()

        similarity: int = 0
        for item in self._list_a:
            similarity += item * self._list_b.count(item)

        return str(similarity)
