"""Solutions for Advent of Code 2024 - Day 13."""

import re
from dataclasses import dataclass, field

from aoc import DaySolution

Movement = tuple[int, int]
Position = list[int, int]
Presses = tuple[int, int]


@dataclass
class ClawMachine:
    """Model for a claw machine."""

    button_a: Movement
    button_b: Movement
    prize_position: Position
    claw_position: Position = field(default_factory=lambda: [0, 0])

    @property
    def max_a(self) -> int:
        """How many time can A be pressed before passing the prize."""
        return min(
            self.prize_position[0] // self.button_a[0],
            self.prize_position[1] // self.button_a[1],
        )

    def reset(self) -> None:
        """Reset het claw position."""
        self.claw_position = [0, 0]

    def press_button_a(self, count: int = 1) -> None:
        """Press button a.

        Moves the claw position.

        Args:
            count: the amount of times to press the button.
        """
        self.claw_position[0] += count * self.button_a[0]
        self.claw_position[1] += count * self.button_a[1]

    def press_button_b(self, count: int = 1) -> None:
        """Press button b.

        Moves the claw position.

        Args:
            count: the amount of times to press the button.
        """
        self.claw_position[0] += count * self.button_b[0]
        self.claw_position[1] += count * self.button_b[1]

    @property
    def is_on_prize(self) -> bool:
        """Property that defines if we are on the prize.

        Returns:
            True when the `position` is on the prize position, ohterwise False.
        """
        return self.claw_position == self.prize_position


class Day13(DaySolution):
    """Solution for Day 13.

    Link: https://adventofcode.com/2024/day/13

    Needed for this solution:
    -   A `input` file from the Advent of Code website. This can be found at
        the link above. Give the location of this file in the `input_file`
        argument of the constructor for the object.
    """

    def __init__(self, input_file: str) -> None:
        """Set internal values."""
        self._input_file = input_file
        self._loaded_data = False
        self._claw_machines: list[ClawMachine] = []

    def _load_data(self) -> None:
        """Load data from the input file."""
        if self._loaded_data:
            return

        with open(self._input_file, encoding='utf-8') as file:
            all_matches = re.findall(
                r'(^Button A: X\+(\d+), Y\+(\d+)$\n)(Button B: X\+(\d+), Y\+(\d+)$\n)(Prize: X\=(\d+), Y\=(\d+))',
                file.read(),
                re.MULTILINE,
            )
        for match in all_matches:
            self._claw_machines.append(
                ClawMachine(
                    button_a=(int(match[1]), int(match[2])),
                    button_b=(int(match[4]), int(match[5])),
                    prize_position=[int(match[7]), int(match[8])],
                )
            )

    def get_minimum_price(self, machine: ClawMachine) -> int:
        """Get the minimum price to win a claw machine.

        Args:
            machine: the machine object.

        Returns:
            0 if the game is unwinnable or a integer with the minimum price
            to win the game.
        """
        minimum_price: int | None = None
        current_price = 1
        while not minimum_price:
            # This number is incorrect, but I have no idea what it should be.
            # The puzzle was right _with_ this number though.
            if current_price >= 3000:
                break

            # Get the possible button presses for this price
            presses: list[Presses] = [
                (a_presses, current_price - (a_presses * 3))
                for a_presses in range(0, 100)
                if current_price - (a_presses * 3) >= 0
                and current_price - (a_presses * 3) <= 100
            ]

            # Try all presses out
            for press in presses:
                machine.reset()
                machine.press_button_a(press[0])
                machine.press_button_b(press[1])
                if machine.is_on_prize:
                    minimum_price = current_price
                    break

            current_price += 1

        return minimum_price or 0

    def solve_puzzle_one(self) -> str:
        """Solve puzzle one."""
        self._load_data()

        minimum_prices = [
            self.get_minimum_price(machine) for machine in self._claw_machines
        ]

        return str(sum(minimum_prices))

    def solve_puzzle_two(self) -> str:
        """Solve puzzle two."""
        self._load_data()
        return ''
