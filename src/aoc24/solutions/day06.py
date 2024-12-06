"""Solutions for Advent of Code 2024 - Day 6."""

from aoc import DaySolution
from enum import Enum


class GuardDirection(int, Enum):
    """Walking direction for a guard."""

    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Day06(DaySolution):
    """Solution for Day 06.

    Link: https://adventofcode.com/2024/day/5

    Needed for this solution:
    -   A `input` file from the Advent of Code website. This can be found at
        the link above. Give the location of this file in the `input_file`
        argument of the constructor for the object.
    """

    def __init__(self, input_file: str) -> None:
        """Set internal values."""
        self._input_file = input_file
        self._map: list[list[str]] = []
        self._guard_position: tuple[int, int] = (0, 0)
        self._guard_direction: GuardDirection = GuardDirection.NORTH
        self._updates: list[list[int]] = []

    def _load_data(self) -> None:
        """Load data from the input file."""
        with open(self._input_file, encoding='utf-8') as file:
            self._map = [list(line.strip()) for line in file.readlines()]

        self._get_current_position()
        self._guard_direction: GuardDirection = GuardDirection.NORTH

    def _get_current_position(self) -> None:
        """Get the current position of the guard."""
        for y in range(len(self._map)):
            for x in range(0, len(self._map[y])):
                if self._map[y][x] == '^':
                    self._guard_position = (x, y)
                    return

    def _is_valid_position(self, x: int, y: int) -> bool:
        """Check if the given position is valid.

        Args:
            x: the x position.
            y: the y position.

        Returns:
            True if we are on the map, False if we aren't.
        """
        return (
            x >= 0 and y >= 0 and y < len(self._map) and x < len(self._map[y])
        )

    def _one_step_forward(self) -> bool:
        """Move the guard one step forward.

        Moves on step in the current direction.

        Returns:
            True if the move was successful. False if the move wasn't due to
            a obstruction.
        """
        new_x, new_y = self._guard_position
        if self._guard_direction == GuardDirection.NORTH:
            new_y -= 1
        elif self._guard_direction == GuardDirection.SOUTH:
            new_y += 1
        elif self._guard_direction == GuardDirection.WEST:
            new_x -= 1
        elif self._guard_direction == GuardDirection.EAST:
            new_x += 1

        if self._is_valid_position(new_x, new_y):
            character_on_new_position = self._map[new_y][new_x]
            if character_on_new_position not in ('.', '^'):
                return False
            self._map[self._guard_position[1]][self._guard_position[0]] = '.'
            self._map[new_y][new_x] = '^'

        self._guard_position = (new_x, new_y)
        return True

    def _turn(self) -> None:
        """Turn the direction of the guard."""
        self._guard_direction = GuardDirection(
            (int(self._guard_direction) + 1) % 4
        )
        pass

    def _get_all_visited_positions(self) -> set[tuple[int, int]]:
        """Get all positions that are visited."""
        visited_positions: set[tuple[int, int]] = set()
        while self._is_valid_position(*self._guard_position):
            if self._one_step_forward() and self._is_valid_position(
                *self._guard_position
            ):
                visited_positions.add(self._guard_position)
            else:
                self._turn()

        return visited_positions

    def solve_puzzle_one(self) -> str:
        """Solve puzzle one."""
        self._load_data()
        return str(len(self._get_all_visited_positions()))

    def _is_loop(self) -> bool:
        """Check if there is a loop by walking around.

        If we get at the same position in the same direction again, we are in
        a loop.

        Returns:
            True if we are in loop, False if we aren't.
        """
        visited_positions: list[tuple[int, int, GuardDirection]] = []
        turns = 0
        while self._is_valid_position(*self._guard_position):
            if self._one_step_forward() and self._is_valid_position(
                *self._guard_position
            ):
                turns = 0
                new_pos = (
                    self._guard_position[0],
                    self._guard_position[1],
                    self._guard_direction,
                )
                visited_positions.append(new_pos)
                if visited_positions.count(new_pos) > 1:
                    return True
            else:
                self._turn()
                turns += 1
                if turns == 4:
                    return True

        return False

    def solve_puzzle_two(self) -> str:
        """Solve puzzle two."""
        self._load_data()
        start_position = self._guard_position
        start_direction = self._guard_direction
        loops: set[tuple[int, int]] = set()

        check_positions = self._get_all_visited_positions()
        i = 0
        for x, y in check_positions:
            if self._map[y][x] in ('.', '^'):
                self._guard_position = start_position
                self._guard_direction = start_direction
                self._map[y][x] = '#'
                if self._is_loop():
                    loops.add((x, y))
                self._map[y][x] = '.'
            print(i := i + 1)

        return str(len(loops))
