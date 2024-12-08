"""Solutions for Advent of Code 2024 - Day 8."""

from aoc import DaySolution


class Day08(DaySolution):
    """Solution for Day 08.

    Link: https://adventofcode.com/2024/day/8

    Needed for this solution:
    -   A `input` file from the Advent of Code website. This can be found at
        the link above. Give the location of this file in the `input_file`
        argument of the constructor for the object.
    """

    def __init__(self, input_file: str) -> None:
        """Set internal values."""
        self._input_file = input_file
        self._loaded_data = False
        self._map: list[list[str]] = []

    def _load_data(self) -> None:
        """Load data from the input file."""
        if self._loaded_data:
            return

        with open(self._input_file, encoding='utf-8') as file:
            rows = file.readlines()
            self._map = [list(x.strip()) for x in rows]
        pass

        self._loaded_data = True

    def _get_possible_pairs(
        self, locations: list[tuple[int, int]]
    ) -> list[tuple[tuple[int, int], tuple[int, int]]]:
        """Find all pairs for specific antenna locations.

        Args:
            locations: the locations for the antenna.

        Returns:
            A set with all found locations.
        """
        return_set: list[tuple[tuple[int, int], tuple[int, int]]] = list()
        for location in enumerate(locations):
            for second_location in locations[location[0] + 1 :]:
                return_set.append((location[1], second_location))
        return return_set

    def _get_antinode_for_pair(
        self, pair: tuple[tuple[int, int], tuple[int, int]]
    ) -> tuple[tuple[int, int], tuple[int, int]]:
        """Find the two antinodes for a antenna pair.

        Args:
            pair: a tuple containing two antenna positions.

        Returns:
            A tuple containing the antinode positions.
        """
        diff_x = abs(pair[0][0] - pair[1][0])
        diff_y = abs(pair[0][1] - pair[1][1])

        first_antinode = (pair[0][0] + diff_x, pair[0][1] - diff_y)
        second_antinode = (pair[1][0] - diff_x, pair[1][1] + diff_y)

        if pair[0][0] < pair[1][0]:
            first_antinode = (pair[0][0] - diff_x, pair[0][1] - diff_y)
            second_antinode = (pair[1][0] + diff_x, pair[1][1] + diff_y)

        return (first_antinode, second_antinode)

    def solve_puzzle_one(self) -> str:
        """Solve puzzle one."""
        self._load_data()

        # Create a map with the locations of specific antennas
        antenna_map: dict[str, list[tuple[int, int]]] = {}

        # Get all locations of the antennas
        for y in range(0, len(self._map)):
            for x in range(0, len(self._map[y])):
                if self._map[y][x] != '.':
                    if antenna_map.get(self._map[y][x]):
                        antenna_map[self._map[y][x]].append((x, y))
                    else:
                        antenna_map[self._map[y][x]] = [(x, y)]

        # Loop through all combinations per antenna and find pairs
        pairs: list[tuple[tuple[int, int], tuple[int, int]]] = []
        for locations in antenna_map.values():
            pairs = pairs + self._get_possible_pairs(locations)

        # Find all antinodes for each pair
        antinodes: set[tuple[int, int]] = set()
        for pair in pairs:
            pair_antinodes = self._get_antinode_for_pair(pair)
            for pair_antinode in pair_antinodes:
                if (
                    pair_antinode[0] < len(self._map[0])
                    and pair_antinode[1] < len(self._map)
                    and pair_antinode[0] >= 0
                    and pair_antinode[1] >= 0
                ):
                    antinodes.add(pair_antinode)

        return str(len(antinodes))

    def solve_puzzle_two(self) -> str:
        """Solve puzzle two."""
        self._load_data()

        return ''
