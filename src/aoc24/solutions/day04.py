"""Solutions for Advent of Code 2024 - Day 4."""

from aoc import DaySolution


class Day04(DaySolution):
    """Solution for Day 04.

    Link: https://adventofcode.com/2024/day/4

    Needed for this solution:
    -   A `input` file from the Advent of Code website. This can be found at
        the link above. Give the location of this file in the `input_file`
        argument of the constructor for the object.
    """

    def __init__(self, input_file: str) -> None:
        """Set internal values."""
        self._input_file = input_file
        self._loaded_data = False
        self._letter_grid: list[list[str]] = []

    def _load_data(self) -> None:
        """Load data from the input file."""
        if self._loaded_data:
            return

        with open(self._input_file, encoding='utf-8') as file:
            for line in file:
                self._letter_grid.append(list(line.strip()))
        self._loaded_data = True

    def _count_horizontal(self) -> int:
        """Find the count of occurences horizontal.

        Returns:
            The count of the word XMAS or SAMX in the lines.
        """
        count = 0
        for line in self._letter_grid:
            line_joined = ''.join(line)
            count += line_joined.count('XMAS')
            count += line_joined.count('SAMX')
        return count

    def _count_vertical(self) -> int:
        """Find the count of occurences vertical.

        Returns:
            The count of the word XMAS or SAMX in the columns.
        """
        count = 0
        for row_index in range(0, len(self._letter_grid[0])):
            row_joined = ''.join([r[row_index] for r in self._letter_grid])
            count += row_joined.count('XMAS')
            count += row_joined.count('SAMX')

        return count

    def _count_diagonal(self) -> int:
        """Find the count of occurences diagonal.

        Returns:
            The count of the word XMAS or SAMX in the columns.
        """
        all_words: list[str] = []
        count = 0

        # Left to right downwards
        for y in range(0, len(self._letter_grid) - 3):
            for x in range(0, len(self._letter_grid[y]) - 3):
                new_x = x
                new_y = y
                word = ''
                while len(word) < 4:
                    word += self._letter_grid[new_y][new_x]
                    new_x += 1
                    new_y += 1
                if word in ('XMAS', 'SAMX'):
                    all_words.append(word)

        # Right to left downwards
        for y in range(0, len(self._letter_grid) - 3):
            for x in range(len(self._letter_grid[y]) - 1, 2, -1):
                new_x = x
                new_y = y
                word = ''
                while len(word) < 4:
                    word += self._letter_grid[new_y][new_x]
                    new_x -= 1
                    new_y += 1
                if word in ('XMAS', 'SAMX'):
                    all_words.append(word)

        return len(all_words)

    def _get_diagonal_to_right(self, x: int, y: int, length: int) -> str:
        """Get the diagonal word from a starting position to the right.

        Args:
            x: the x position.
            y: the y position.
            length: the amount of characters to get
        """
        new_x = x
        new_y = y
        word = ''
        while len(word) < length:
            try:
                word += self._letter_grid[new_y][new_x]
            except IndexError:
                break
            new_x += 1
            new_y += 1
        return word

    def _get_diagonal_to_left(self, x: int, y: int, length: int) -> str:
        """Get the diagonal word from a starting position to the left.

        Args:
            x: the x position.
            y: the y position.
            length: the amount of characters to get
        """
        new_x = x
        new_y = y
        word = ''
        while len(word) < length:
            try:
                word += self._letter_grid[new_y][new_x]
            except IndexError:
                break
            new_x -= 1
            if new_x < 0:
                break
            new_y += 1
        return word

    def _count_x_mas(self) -> int:
        """Find the count of occurences of X-MAS.

        This means we have to find all occurences of:

            .M.S.
            ..A..
            .M.S.

        It basically means it's two MAS'es in a X.

        Returns:
            The count of the word word MAS in a X.
        """
        count = 0

        # Left to right downwards
        for y in range(0, len(self._letter_grid)):
            for x in range(0, len(self._letter_grid[y])):
                word_r = self._get_diagonal_to_right(x, y, 3)
                if word_r in ('MAS', 'SAM'):
                    word_l = self._get_diagonal_to_left(x + 2, y, 3)
                    if word_l in ('MAS', 'SAM'):
                        count += 1

        return count

    def solve_puzzle_one(self) -> str:
        """Solve puzzle one."""
        self._load_data()

        count = 0

        count += self._count_horizontal()
        count += self._count_vertical()
        count += self._count_diagonal()

        return str(count)

    def solve_puzzle_two(self) -> str:
        """Solve puzzle two."""
        self._load_data()
        return str(self._count_x_mas())
