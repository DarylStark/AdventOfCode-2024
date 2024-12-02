"""Solutions for Advent of Code 2024 - Day 1."""

from aoc import DaySolution


class Day02(DaySolution):
    """Solution for Day 02.

    Link: https://adventofcode.com/2024/day/2

    Needed for this solution:
    -   A `input` file from the Advent of Code website. This can be found at
        the link above. Give the location of this file in the `input_file`
        argument of the constructor for the object.
    """

    def __init__(self, input_file: str) -> None:
        """Set internal values."""
        self._input_file = input_file
        self._loaded_data = False
        self._list: list[list[int]] = []

    def _load_data(self) -> None:
        """Load data from the input file."""
        if self._loaded_data:
            return

        with open(self._input_file, encoding='utf-8') as file:
            for line in file:
                self._list.append([int(x) for x in line.split()])
        self._loaded_data = True

    def _is_increasing(self, numbers: list[int]) -> bool:
        """Check if a list is "increasing".

        Args:
            numbers: a list of numbers to check.

        Returns:
            True when the list is increasing. False when it isn't.
        """
        last_number: int = numbers[0]
        for number in numbers[1:]:
            if number <= last_number:
                return False
            last_number = number
        return True

    def _is_decreasing(self, numbers: list[int]) -> bool:
        """Check if a list is "decreasing".

        Args:
            numbers: a list of numbers to check.

        Returns:
            True when the list is decreasing. False when it isn't.
        """
        last_number: int = numbers[0]
        for number in numbers[1:]:
            if number >= last_number:
                return False
            last_number = number
        return True

    def _adjecent_numbers(
        self, numbers: list[int], max_difference: int = 3
    ) -> bool:
        """Check if all the numbers are not too far apart.

        Args:
            numbers: a list of numbers to check.
            max_difference: the max two numbers can be apart from each other.

        Returns:
            True when the numbers are not too far apart.
        """
        last_number: int = numbers[0]
        for number in numbers[1:]:
            if (
                max([number, last_number]) - min([number, last_number])
                > max_difference
            ):
                return False
            last_number = number
        return True

    def solve_puzzle_one(self) -> str:
        """Solve puzzle one."""
        self._load_data()

        safe_reports = 0

        for report in self._list:
            # Check the first rule
            if not (
                self._is_increasing(report) or self._is_decreasing(report)
            ):
                continue

            # Check the scond rule
            if self._adjecent_numbers(report, 3):
                safe_reports += 1

        return str(safe_reports)

    def solve_puzzle_two(self) -> str:
        """Solve puzzle two."""
        return ''
