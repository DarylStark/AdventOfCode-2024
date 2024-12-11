"""Solutions for Advent of Code 2024 - Day 11."""

from aoc import DaySolution


class Day11(DaySolution):
    """Solution for Day 11.

    Link: https://adventofcode.com/2024/day/11

    Needed for this solution:
    -   A `input` file from the Advent of Code website. This can be found at
        the link above. Give the location of this file in the `input_file`
        argument of the constructor for the object.
    """

    def __init__(self, input_file: str) -> None:
        """Set internal values."""
        self._input_file = input_file
        self._loaded_data = False
        self._stones: list[int] = []
        self._blinks = 0
        self._cache: dict[tuple[int, int], int] = {}

    def _load_data(self) -> None:
        """Load data from the input file."""
        if self._loaded_data:
            return

        with open(self._input_file, encoding='utf-8') as file:
            self._stones = [int(stone) for stone in file.read().split()]

    def _stone_count(self, value: int, increment: int) -> int:
        """Blink and return the new count of the number.

        Args:
            value: the value for the stone.
            increment: the increment level we are on.

        Returns:
            The amount of stones you get from this specific value.
        """
        if increment == 0:
            return 1

        if (value, increment) in self._cache:
            return self._cache[(value, increment)]

        if value == 0:
            new_value = self._stone_count(1, increment - 1)

        elif len(str(value)) % 2 == 0:
            value_as_string = str(value)
            stone1 = int(value_as_string[0 : len(value_as_string) // 2])
            stone2 = int(value_as_string[len(value_as_string) // 2 :])
            new_value = self._stone_count(
                stone1, increment - 1
            ) + self._stone_count(stone2, increment - 1)
        else:
            new_value = self._stone_count(value * 2024, increment - 1)

        self._cache[(value, increment)] = new_value

        return new_value

    def solve_puzzle_one(self) -> str:
        """Solve puzzle one."""
        self._load_data()

        count = 0
        for stone in self._stones:
            count += self._stone_count(stone, 25)

        return str(count)

    def solve_puzzle_two(self) -> str:
        """Solve puzzle two."""
        self._load_data()

        count = 0
        for stone in self._stones:
            count += self._stone_count(stone, 75)

        return str(count)
