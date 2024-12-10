"""Solutions for Advent of Code 2024 - Day 10."""

from dataclasses import dataclass, field

from aoc import DaySolution

MapLocation = tuple[int, int]


@dataclass
class TrailStart:
    """Structure for a trail."""

    trailhead: MapLocation
    possible_trails: int = 0
    all_endpoints: set[MapLocation] = field(default_factory=set)
    rating: int = 0


class Day10(DaySolution):
    """Solution for Day 10.

    Link: https://adventofcode.com/2024/day/10

    Needed for this solution:
    -   A `input` file from the Advent of Code website. This can be found at
        the link above. Give the location of this file in the `input_file`
        argument of the constructor for the object.
    """

    def __init__(self, input_file: str) -> None:
        """Set internal values."""
        self._input_file = input_file
        self._loaded_data = False
        self._map: list[list[int]] = []
        self._trailstarts: list[TrailStart] = []

    def _load_data(self) -> None:
        """Load data from the input file."""
        if self._loaded_data:
            return

        with open(self._input_file, encoding='utf-8') as file:
            self._map = [
                [int(elevation) for elevation in list(map_line.strip())]
                for map_line in file.readlines()
            ]

    def _find_all_trail_starts(self) -> None:
        """Create all TrailStart objects."""
        self._trailstarts = []
        for y in range(0, len(self._map)):
            for x in range(0, len(self._map[y])):
                if self._map[y][x] == 0:
                    self._trailstarts.append(TrailStart(trailhead=(x, y)))

    def _find_next_step_in_path(
        self, current_location: MapLocation, trail_start: TrailStart
    ) -> None:
        """Find the next step in a specific trail.

        Args:
            current_location: the current location for the trail.
            trail_start: the TrailStart object to update.
        """
        current_elevation = self._map[current_location[1]][current_location[0]]
        if current_elevation == 9:
            trail_start.possible_trails += 1
            trail_start.all_endpoints.add(current_location)
            trail_start.rating += 1
            return

        # Find the next step
        next_elevation = current_elevation + 1
        locations_to_check = [
            (current_location[0] - 1, current_location[1]),
            (current_location[0] + 1, current_location[1]),
            (current_location[0], current_location[1] - 1),
            (current_location[0], current_location[1] + 1),
        ]
        for location_to_check in locations_to_check:
            if (
                location_to_check[0] >= 0
                and location_to_check[0] < len(self._map[0])
                and location_to_check[1] >= 0
                and location_to_check[1] < len(self._map)
            ):
                elevation = self._map[location_to_check[1]][
                    location_to_check[0]
                ]
                if elevation == next_elevation:
                    self._find_next_step_in_path(
                        location_to_check, trail_start
                    )

    def _find_all_trails(self) -> None:
        """Fill in all trails in the TrailStart objects."""
        for trailstart in self._trailstarts:
            self._find_next_step_in_path(trailstart.trailhead, trailstart)

    def solve_puzzle_one(self) -> str:
        """Solve puzzle one."""
        self._load_data()
        self._find_all_trail_starts()
        self._find_all_trails()

        # Find the sum of all endpoints for all trailstarts
        count = sum([len(t.all_endpoints) for t in self._trailstarts])

        return str(count)

    def solve_puzzle_two(self) -> str:
        """Solve puzzle two."""
        self._load_data()
        self._find_all_trail_starts()
        self._find_all_trails()

        # Find the sum of all endpoints for all trailstarts
        count = sum([t.rating for t in self._trailstarts])

        return str(count)
