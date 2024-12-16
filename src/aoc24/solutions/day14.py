"""Solutions for Advent of Code 2024 - Day 14."""

import re
from aoc import DaySolution
from dataclasses import dataclass

Movement = tuple[int, int]
Position = list[int, int]
Size = tuple[int, int]


@dataclass
class Robot:
    """Model for a dataclass."""

    position: Position
    velocity: Movement

    def move(self, count: int, map_size: Size) -> None:
        """Move the robot.

        Args:
            count: how many times (seconds) to move the robot.
            map_size: the size of the map.
        """
        for index in (0, 1):
            self.position[index] = (
                self.position[index] + (self.velocity[index] * count)
            ) % map_size[index]


class Day14(DaySolution):
    """Solution for Day 14.

    Link: https://adventofcode.com/2024/day/14

    Needed for this solution:
    -   A `input` file from the Advent of Code website. This can be found at
        the link above. Give the location of this file in the `input_file`
        argument of the constructor for the object.
    """

    def __init__(self, input_file: str, map_size: Size) -> None:
        """Set internal values.

        Args:
            input_file: the file with the input data.
            map_size: the size of the map.
        """
        self._input_file = input_file
        self._loaded_data = False
        self._robots: list[Robot] = []
        self._map_size = map_size

    def _load_data(self) -> None:
        """Load data from the input file."""
        if self._loaded_data:
            return

        with open(self._input_file, encoding='utf-8') as file:
            robots = file.readlines()
        for robot in robots:
            details = list(
                map(
                    int,
                    re.findall(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', robot)[
                        0
                    ],
                )
            )
            self._robots.append(
                Robot(
                    position=[details[0], details[1]],
                    velocity=(details[2], details[3]),
                )
            )
            pass

    def _get_quadrant_for_position(self, position: Position) -> int:
        """Retrieve a quadrant for a specific position.

        Args:
            position: the position to calculate the position for.

        Returns:
            The position (0 is the left on top, 1 right on top, 2 left bottom,
            3 right bottom). If it returns -1, the position is not in a
            quadrant, which basically means it is between two quadrants.
        """
        quadrant_width = self._map_size[0] // 2
        quadrant_height = self._map_size[1] // 2

        if position[0] == quadrant_width or position[1] == quadrant_height:
            return -1

        qx = 0
        if position[0] > quadrant_width:
            qx = 1

        qy = 0
        if position[1] > quadrant_height:
            qy = 1

        return (qy * 2) + qx

    def _move_all_robots(self, count: int) -> None:
        """Move all robots.

        Args:
            count: how many times (seconds) to move the robots.
        """
        for robot in self._robots:
            robot.move(count, self._map_size)

    def solve_puzzle_one(self) -> str:
        """Solve puzzle one."""
        self._load_data()

        # Move the robots
        self._move_all_robots(100)

        # Get the count of robots per quadrant
        quadrant_robot_count: list[int] = [0, 0, 0, 0, 0]
        for robot in self._robots:
            quadrant_robot_count[
                self._get_quadrant_for_position(robot.position)
            ] += 1

        return str(
            quadrant_robot_count[0]
            * quadrant_robot_count[1]
            * quadrant_robot_count[2]
            * quadrant_robot_count[3]
        )

    def solve_puzzle_two(self) -> str:
        """Solve puzzle two."""
        self._load_data()
        return ''
