"""Solutions for Advent of Code 2024 - Day 3."""

from aoc import DaySolution
import re


class Day03(DaySolution):
    """Solution for Day 03.

    Link: https://adventofcode.com/2024/day/3

    Needed for this solution:
    -   A `input` file from the Advent of Code website. This can be found at
        the link above. Give the location of this file in the `input_file`
        argument of the constructor for the object.
    """

    def __init__(self, input_file: str) -> None:
        """Set internal values."""
        self._input_file = input_file
        self._loaded_data = False
        self._file_data: str = ''

    def _load_data(self) -> None:
        """Load data from the input file."""
        if self._loaded_data:
            return

        with open(self._input_file, encoding='utf-8') as file:
            self._file_data = file.read()
        self._loaded_data = True

    def solve_puzzle_one(self) -> str:
        """Solve puzzle one."""
        self._load_data()

        instructions = [
            (int(x[0]), int(x[1]))
            for x in re.findall(r'mul\((\d+),(\d+)\)', self._file_data)
        ]

        total = 0
        for multiply in instructions:
            total += multiply[0] * multiply[1]
        return str(total)

    def solve_puzzle_two(self) -> str:
        """Solve puzzle two."""
        self._load_data()

        all_instructions = re.findall(
            r'mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))',
            self._file_data,
        )

        enabled = True
        total = 0
        for instruction in all_instructions:
            if instruction[3] == "don't()":
                enabled = False
            elif instruction[2] == 'do()':
                enabled = True
            elif enabled:
                total += int(instruction[0]) * int(instruction[1])
        return str(total)
