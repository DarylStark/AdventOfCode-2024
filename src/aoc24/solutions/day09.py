"""Solutions for Advent of Code 2024 - Day 9."""

from aoc import DaySolution


class Day09(DaySolution):
    """Solution for Day 09.

    Link: https://adventofcode.com/2024/day/9

    Needed for this solution:
    -   A `input` file from the Advent of Code website. This can be found at
        the link above. Give the location of this file in the `input_file`
        argument of the constructor for the object.
    """

    def __init__(self, input_file: str) -> None:
        """Set internal values."""
        self._input_file = input_file
        self._loaded_data = False
        self._drive: str = ''
        self._drive_list: list[int | None] = []

    def _load_data(self) -> None:
        """Load data from the input file."""
        if self._loaded_data:
            return

        with open(self._input_file, encoding='utf-8') as file:
            self._drive = file.read()

    def _create_drive_list(self) -> None:
        """Create a Python list with the drive index."""
        id = 0
        for idx, size in enumerate(self._drive):
            size = int(size)
            if idx % 2 == 0:
                self._drive_list.extend([id] * size)
                id += 1
            else:
                self._drive_list.extend([None] * size)

    def _get_first_empty_index(self) -> int:
        """Get the fist emtpy place on the drive.

        Returns:
            The index of the first empty block.
        """
        return self._drive_list.index(None)

    def _defgrament_list(self) -> None:
        """Defragment the file list."""
        for block in range(len(self._drive_list), 0, -1):
            block_value = self._drive_list[block - 1]

            if block_value:
                # Find the first empty index
                first_empty = self._get_first_empty_index()
                if first_empty >= block:
                    break

                # Move the block
                self._drive_list[first_empty] = block_value
                self._drive_list[block - 1] = None

    def _get_checksum(self) -> int:
        """Calculate the checksum for the drive.

        Returns:
            The checksum as integer.
        """
        checksum = 0
        for idx, value in enumerate(self._drive_list):
            if value:
                checksum += idx * value
        return checksum

    def solve_puzzle_one(self) -> str:
        """Solve puzzle one."""
        self._load_data()
        self._create_drive_list()
        self._defgrament_list()
        return str(self._get_checksum())

    def solve_puzzle_two(self) -> str:
        """Solve puzzle two."""
        self._load_data()
        return ''
