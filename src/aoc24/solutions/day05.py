"""Solutions for Advent of Code 2024 - Day 5."""

import re

from aoc import DaySolution


class Day05(DaySolution):
    """Solution for Day 05.

    Link: https://adventofcode.com/2024/day/5

    Needed for this solution:
    -   A `input` file from the Advent of Code website. This can be found at
        the link above. Give the location of this file in the `input_file`
        argument of the constructor for the object.
    """

    def __init__(self, input_file: str) -> None:
        """Set internal values."""
        self._input_file = input_file
        self._loaded_data = False
        self._rules: list[tuple[int, int]] = []
        self._updates: list[list[int]] = []

    def _load_data(self) -> None:
        """Load data from the input file."""
        if self._loaded_data:
            return

        with open(self._input_file, encoding='utf-8') as file:
            data = file.read()
        self._rules = [
            (int(first), int(second))
            for first, second in re.findall(r'(\d+)\|(\d+)', data)
        ]
        self._updates = [
            [int(page) for page in update[0].split(',')]
            for update in re.findall(r'^(\d+(,\d+)*)$', data, re.MULTILINE)
        ]
        self._loaded_data = True

    def _is_valid_update(self, update: list[int]) -> bool:
        """Check if a update is valid.

        Args:
            update: the update

        Returns:
            True on a vaild update, False on a invalid update.
        """
        for page in enumerate(update):
            # Find the page and see if the "most important page" is after it
            for rule in self._rules:
                if rule[1] == page[1] and update[page[0] + 1 :].count(rule[0]):
                    return False

        return True

    def solve_puzzle_one(self) -> str:
        """Solve puzzle one."""
        self._load_data()

        sum = 0

        # Loop through every update
        for update in self._updates:
            if self._is_valid_update(update):
                # Find the middle number
                middle_number = update[len(update) // 2]
                sum += middle_number

        return str(sum)

    def solve_puzzle_two(self) -> str:
        """Solve puzzle two."""
        self._load_data()
        return ''
