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

    def _load_data(self) -> None:
        """Load data from the input file."""
        if self._loaded_data:
            return

        with open(self._input_file, encoding='utf-8') as file:
            self._stones = [int(stone) for stone in file.read().split()]

    def _blink(self) -> None:
        """Blink one time.

        Will execute the required rules on the stonelist.
        """
        stone_index = 0
        self._blinks += 1
        while True:
            if stone_index >= len(self._stones):
                break

            if self._stones[stone_index] == 0:
                # Stone is `0`, we replace it by a stoned with `1`
                self._stones[stone_index] = 1
                stone_index += 1
                continue

            if len(str(self._stones[stone_index])) % 2 == 0:
                # Stone has a even "length"
                stone_engraving = str(self._stones[stone_index])
                stone1 = int(stone_engraving[0 : len(stone_engraving) // 2])
                stone2 = int(stone_engraving[len(stone_engraving) // 2 :])
                self._stones[stone_index] = stone1
                self._stones.insert(stone_index + 1, stone2)
                stone_index += 2
                continue

            self._stones[stone_index] *= 2024
            stone_index += 1

    def solve_puzzle_one(self) -> str:
        """Solve puzzle one."""
        self._load_data()

        for _ in range(0, 25):
            self._blink()

        return str(len(self._stones))

    def solve_puzzle_two(self) -> str:
        """Solve puzzle two."""
        self._load_data()
        return ''
