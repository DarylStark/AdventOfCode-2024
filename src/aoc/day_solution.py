"""Module with a abstract class for solutions."""

from abc import ABC, abstractmethod


class DaySolution(ABC):
    """Abstract class for solutions.

    Should be implemented by specific solutions.
    """

    @abstractmethod
    def solve_puzzle_one(self) -> str:
        """Solve the first puzzle and return the solution.

        Returns:
            The solution as a string.
        """

    @abstractmethod
    def solve_puzzle_two(self) -> str:
        """Solve the second puzzle and return the solution.

        Returns:
            The solution as a string.
        """
