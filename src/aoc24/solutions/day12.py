"""Solutions for Advent of Code 2024 - Day 12."""

from tabnanny import check
from aoc import DaySolution
from dataclasses import dataclass, field


@dataclass
class Region:
    """Dataclass for a region."""

    character: str
    plots: set[tuple[int, int]] = field(default_factory=set)

    @property
    def area(self) -> int:
        """Get the area for a Region.

        Returns:
            The area for the region as integer.
        """
        return len(self.plots)

    @property
    def perimeter(self) -> int:
        """Get the area for the perimeter.

        Returns:
            The perimeter for the region as integer.
        """
        perimeter = 0
        for plot in self.plots:
            check_locations = [
                (plot[0] - 1, plot[1]),
                (plot[0] + 1, plot[1]),
                (plot[0], plot[1] - 1),
                (plot[0], plot[1] + 1),
            ]
            for check_location in check_locations:
                if check_location not in self.plots:
                    perimeter += 1
        return perimeter


class Day12(DaySolution):
    """Solution for Day 12.

    Link: https://adventofcode.com/2024/day/12

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
        self._regions: list[Region] = []

    def _load_data(self) -> None:
        """Load data from the input file."""
        if self._loaded_data:
            return

        with open(self._input_file, encoding='utf-8') as file:
            self._map = [list(x.strip()) for x in file.readlines()]

    def _get_surrounding_plots(
        self, region: Region, position: tuple[int, int]
    ) -> None:
        """Add all surrounding plots with the same character.

        Args:
            region: the region to add it to.
            position: the pos to look at.
        """
        region.plots.add(position)
        check_locations = [
            (position[0] - 1, position[1]),
            (position[0] + 1, position[1]),
            (position[0], position[1] - 1),
            (position[0], position[1] + 1),
        ]
        for check_location in check_locations:
            if (
                check_location[0] >= 0
                and check_location[1] >= 0
                and check_location[0] < len(self._map[0])
                and check_location[1] < len(self._map)
                and check_location not in region.plots
                and self._map[check_location[1]][check_location[0]]
                == region.character
            ):
                self._get_surrounding_plots(region, check_location)

    def _find_all_regions(self) -> None:
        """Find all regions in the map."""
        scouted_plots: set[tuple[int, int]] = set()
        for y in range(0, len(self._map)):
            for x in range(0, len(self._map[y])):
                if (x, y) in scouted_plots:
                    continue

                # Create a new region
                new_region = Region(character=self._map[y][x])
                self._get_surrounding_plots(new_region, (x, y))

                # Add the checked plots
                for plot in new_region.plots:
                    scouted_plots.add(plot)
                self._regions.append(new_region)

    def solve_puzzle_one(self) -> str:
        """Solve puzzle one."""
        self._load_data()
        self._find_all_regions()

        total_price = 0
        for a in self._regions:
            total_price += a.area * a.perimeter

        return str(total_price)

    def solve_puzzle_two(self) -> str:
        """Solve puzzle two."""
        self._load_data()
        return ''
