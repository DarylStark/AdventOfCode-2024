"""Module that contains the `main` method.

This method is ran when the script is ran as a module and when it is ran as a
executable script.
"""

from rich.console import Console

from aoc.advent_of_code import AdventOfCode

from .solutions import Day01


def main() -> None:
    """Main function for the application."""
    aoc24 = AdventOfCode()
    console = Console()

    # Add solutions
    aoc24.add_solution(1, Day01('data/day01-input.txt'))

    # Print solutions
    console.print('[yellow][bold]Advent of Code 2024!![/bold][/yellow]')
    console.print('[gray]By Daryl Stark[/gray]')
    console.print('')
    for day in range(1, 25):
        solution = aoc24.get_solution(day)
        if solution is not None:
            console.print(f'[bold]Day {day:02}[/bold]: ', end='')
            console.print(f'Puzzle 1: {solution.solve_puzzle_one()}')
            console.print(
                ' ' * 8, f'Puzzle 2: {solution.solve_puzzle_two()}', sep=''
            )
