"""Module with the AdventOfCode class."""

from .day_solution import DaySolution


class AdventOfCode:
    """Class that can be used for the solutions of Advent of Code."""

    def __init__(self) -> None:
        """Set internal values."""
        self._solutions: dict[int, DaySolution] = {}

    def add_solution(self, day: int, solution: DaySolution) -> None:
        """Add a solution to the list of solutions.

        Args:
            day: the day for which the solution is. Can be 1 to 24.
            solution: the solution to add.
        """
        if day < 1 or day > 24:
            raise ValueError('Invalid day.')
        self._solutions[day] = solution

    def get_solution(self, day: int) -> DaySolution | None:
        """Get the solution for a specific day.

        Args:
            day: the day for which the solution is. Can be 1 to 24.

        Returns:
            The solution for the specific day or None if it does not exist.
        """
        solution = self._solutions.get(day, None)
        return solution
