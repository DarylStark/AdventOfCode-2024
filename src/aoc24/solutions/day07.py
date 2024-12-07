"""Solutions for Advent of Code 2024 - Day 7."""

from aoc import DaySolution


class Day07(DaySolution):
    """Solution for Day 07.

    Link: https://adventofcode.com/2024/day/7

    Needed for this solution:
    -   A `input` file from the Advent of Code website. This can be found at
        the link above. Give the location of this file in the `input_file`
        argument of the constructor for the object.
    """

    def __init__(self, input_file: str) -> None:
        """Set internal values."""
        self._input_file = input_file
        self._loaded_data = False
        self._calibrations: list[tuple[int, list[int]]] = []

    def _load_data(self) -> None:
        """Load data from the input file."""
        if self._loaded_data:
            return

        with open(self._input_file, encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                splitted = line.split(':')
                result = int(splitted[0].strip())
                equations = [int(eq) for eq in splitted[1].strip().split(' ')]
                self._calibrations.append((result, equations))

    def _is_correct_calibration(
        self, required_result: int, equations: list[int]
    ) -> bool:
        """Determine if the result can be generated from the equations.

        Args:
            required_result: the needed result.
            equations: the numbers to generate the result with.

        Returns:
            True if the required result can be achieved, Otherwise False.
        """
        if len(equations) == 2:
            if equations[0] + equations[1] == required_result:
                return True
            return equations[0] * equations[1] == required_result

        if self._is_correct_calibration(
            required_result, [equations[0] + equations[1], *equations[2:]]
        ):
            return True
        return self._is_correct_calibration(
            required_result, [equations[0] * equations[1], *equations[2:]]
        )

    def solve_puzzle_one(self) -> str:
        """Solve puzzle one."""
        self._load_data()

        # Loop through each calibration and find the correct operators
        correct = 0
        for calibration in self._calibrations:
            result = calibration[0]
            equations = calibration[1]
            if self._is_correct_calibration(result, equations):
                correct += result

        return str(correct)

    def solve_puzzle_two(self) -> str:
        """Solve puzzle two."""
        self._load_data()
        return ''
