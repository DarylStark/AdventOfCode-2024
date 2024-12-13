"""Solutions for Advent of Code 2024 - Day 12."""

from tabnanny import check
from aoc import DaySolution
from dataclasses import dataclass, field


@dataclass
class Region:
    """Dataclass for a region."""

    character: str
    plots: set[tuple[int, int]] = field(default_factory=set)
    perimeter_plots: list[tuple[int, int]] = field(default_factory=list)

    def generate_perimeter_plots(self) -> None:
        """Fill the `perimeter_plots` list."""
        self.perimeter_plots = []
        for plot in self.plots:
            check_locations = [
                (plot[0] - 1, plot[1]),
                (plot[0] + 1, plot[1]),
                (plot[0], plot[1] - 1),
                (plot[0], plot[1] + 1),
            ]
            for check_location in check_locations:
                if check_location not in self.plots:
                    self.perimeter_plots.append(check_location)

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
        if len(self.perimeter_plots) == 0:
            self.generate_perimeter_plots()
        return len(self.perimeter_plots)

    @property
    def sides(self) -> int:
        """Get the amount of sites for the region.

        This function is a mess. It took quite a long time before I found a
        (working) way of getting the correct answer for this, so I had to play
        around a bit, which resulted in the code below. We need to refactor it
        but to be fair; the puzzle was correct, so it is not that important
        anymore.

        Returns:
            The amount of sides for the region as a integer.
        """
        if len(self.perimeter_plots) == 0:
            self.generate_perimeter_plots()

        def horizontal_l_wall_count(plot: tuple[int, int]) -> int:
            return int((plot[0], plot[1] - 1) in self.plots)

        def horizontal_r_wall_count(plot: tuple[int, int]) -> int:
            return int((plot[0], plot[1] + 1) in self.plots)

        def vertical_t_wall_count(plot: tuple[int, int]) -> int:
            return int((plot[0] - 1, plot[1]) in self.plots)

        def vertical_b_wall_count(plot: tuple[int, int]) -> int:
            return int((plot[0] + 1, plot[1]) in self.plots)

        plots: dict[tuple[int, int], list[int, int, set[int]]] = {
            plot: [
                horizontal_l_wall_count(plot),
                horizontal_r_wall_count(plot),
                vertical_t_wall_count(plot),
                vertical_b_wall_count(plot),
                set(),
            ]
            for plot in self.perimeter_plots
        }

        used_sides: set[int] = set()

        def set_side_index_for_horizonal_l_side(
            plot: tuple[int, int], side_index: int
        ) -> None:
            plot_value = plots.get(plot)
            if not plot_value:
                return

            if plot_value[0] > 0 and side_index not in plot_value[4]:
                plot_value[0] -= 1
                plot_value[4].add(side_index)
                used_sides.add(side_index)
                set_side_index_for_horizonal_l_side(
                    (plot[0] - 1, plot[1]), side_index
                )
                set_side_index_for_horizonal_l_side(
                    (plot[0] + 1, plot[1]), side_index
                )

        def set_side_index_for_horizonal_r_side(
            plot: tuple[int, int], side_index: int
        ) -> None:
            plot_value = plots.get(plot)
            if not plot_value:
                return

            if plot_value[1] > 0 and side_index not in plot_value[4]:
                plot_value[1] -= 1
                plot_value[4].add(side_index)
                used_sides.add(side_index)
                set_side_index_for_horizonal_r_side(
                    (plot[0] - 1, plot[1]), side_index
                )
                set_side_index_for_horizonal_r_side(
                    (plot[0] + 1, plot[1]), side_index
                )

        def set_side_index_for_vertical_t_side(
            plot: tuple[int, int], side_index: int
        ) -> None:
            plot_value = plots.get(plot)
            if not plot_value:
                return

            if plot_value[2] > 0 and side_index not in plot_value[4]:
                plot_value[2] -= 1
                plot_value[4].add(side_index)
                used_sides.add(side_index)
                set_side_index_for_vertical_t_side(
                    (plot[0], plot[1] - 1), side_index
                )
                set_side_index_for_vertical_t_side(
                    (plot[0], plot[1] + 1), side_index
                )

        def set_side_index_for_vertical_b_side(
            plot: tuple[int, int], side_index: int
        ) -> None:
            plot_value = plots.get(plot)
            if not plot_value:
                return

            if plot_value[3] > 0 and side_index not in plot_value[4]:
                plot_value[3] -= 1
                plot_value[4].add(side_index)
                used_sides.add(side_index)
                set_side_index_for_vertical_b_side(
                    (plot[0], plot[1] - 1), side_index
                )
                set_side_index_for_vertical_b_side(
                    (plot[0], plot[1] + 1), side_index
                )

        side_index = 0
        while sum([plot[0] for plot in plots.values()]) > 0:
            for plot in plots:
                set_side_index_for_horizonal_l_side(plot, side_index)
                side_index += 1

        while sum([plot[1] for plot in plots.values()]) > 0:
            for plot in plots:
                set_side_index_for_horizonal_r_side(plot, side_index)
                side_index += 1

        while sum([plot[2] for plot in plots.values()]) > 0:
            for plot in plots:
                set_side_index_for_vertical_t_side(plot, side_index)
                side_index += 1

        while sum([plot[3] for plot in plots.values()]) > 0:
            for plot in plots:
                set_side_index_for_vertical_b_side(plot, side_index)
                side_index += 1

        return len(used_sides)

    @property
    def price(self) -> int:
        """Get the price for the perimeter.

        Returns:
            The price as integer.
        """
        return self.area * self.perimeter

    @property
    def discounted_price(self) -> int:
        """Get the discounted price for the perimeter.

        Returns:
            The price as integer.
        """
        return self.area * self.sides


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
        self._regions = []
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
        for region in self._regions:
            total_price += region.price

        return str(total_price)

    def solve_puzzle_two(self) -> str:
        """Solve puzzle two."""
        self._load_data()
        self._find_all_regions()

        total_price = 0
        for region in self._regions:
            total_price += region.discounted_price

        return str(total_price)
