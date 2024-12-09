"""Solutions for Advent of Code 2024 - Day 9."""

from operator import index
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
        self._drive_list_files: list[tuple[None | int, int]] = []

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
            size_int = int(size)
            if idx % 2 == 0:
                self._drive_list.extend([id] * size_int)
                id += 1
            else:
                self._drive_list.extend([None] * size_int)

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

    def _create_file_list(self) -> None:
        """Create a list with all files and sizes.

        This list can be used to defragment the drive based on files instead of
        sectors.
        """
        id = 0
        for idx, size in enumerate(self._drive):
            size_int = int(size)
            if idx % 2 == 0:
                self._drive_list_files.append((id, size_int))
                id += 1
            else:
                self._drive_list_files.append((None, size_int))

    def _get_first_empty_index_of_size(
        self, size: int, max_index: int
    ) -> tuple[int | None, tuple[None | int, int] | None]:
        """Get the fist emtpy place on the drive with a specific space.

        Args:
            size: the size to search for.
            max_index: the maximum index to search

        Returns:
            The index of the first empty block with at least the correct amount
            of space.
        """
        for idx, fd in enumerate(self._drive_list_files):
            if idx >= max_index:
                break

            if fd[0] is None and fd[1] >= size:
                return (idx, fd)
        return (None, None)

    def _get_checksum_file_list(self) -> int:
        """Calculate the checksum for the drive.

        Returns:
            The checksum as integer.
        """
        # Recreate the '_drive_list' array
        self._drive_list = []
        for idx, item in enumerate(self._drive_list_files):
            size_int = item[1]
            if item[0] is not None:
                self._drive_list.extend([item[0]] * size_int)
            else:
                self._drive_list.extend([None] * size_int)

        return self._get_checksum()

    def solve_puzzle_one(self) -> str:
        """Solve puzzle one."""
        self._load_data()
        self._create_drive_list()
        self._defgrament_list()
        return str(self._get_checksum())

    def solve_puzzle_two(self) -> str:
        """Solve puzzle two."""
        self._load_data()
        self._create_file_list()

        indexes_done: list[int] = []

        for file in range(len(self._drive_list_files), 0, -1):
            current_block = self._drive_list_files[file - 1]
            if current_block[0]:
                if current_block[0] in indexes_done:
                    continue
                indexes_done.append(current_block[0])
                block_to_fill = self._get_first_empty_index_of_size(
                    current_block[1], file
                )
                if block_to_fill[0] and block_to_fill[1]:
                    index_to_empty = file - 1
                    # Check if we need to resize the current empty block
                    if block_to_fill[1][1] > current_block[1]:
                        self._drive_list_files[block_to_fill[0]] = (
                            None,
                            block_to_fill[1][1] - current_block[1],
                        )
                        self._drive_list_files.insert(
                            block_to_fill[0],
                            (current_block[0], current_block[1]),
                        )
                        index_to_empty = file
                    else:
                        # We can move it directly
                        self._drive_list_files[block_to_fill[0]] = (
                            current_block[0],
                            current_block[1],
                        )

                    self._drive_list_files[index_to_empty] = (
                        None,
                        current_block[1],
                    )

        return str(self._get_checksum_file_list())
