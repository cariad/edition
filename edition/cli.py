from argparse import ArgumentParser
from enum import IntEnum, auto, unique
from typing import IO, List

from edition import __version__


@unique
class CliTask(IntEnum):
    HELP = auto()
    VERSION = auto()


class Cli:
    def __init__(self, args: List[str]) -> None:
        self._parser = ArgumentParser(
            description="Lightweight documentation generator",
            epilog="Made with love by Cariad Eccleston: https://github.com/cariad/edition",
        )

        self._parser.add_argument(
            "--version",
            help="show version and exit",
            action="store_true",
        )

        self._task = CliTask.HELP
        parsed = self._parser.parse_args(args)

        if parsed.version:
            self._task = CliTask.VERSION

    @property
    def task(self) -> CliTask:
        """Gets the task that this CLI invocation will perform."""

        return self._task

    def invoke(self, writer: IO[str]) -> int:
        """
        Invokes the prescribed task.

        Returns the shell exit code.
        """

        if self._task == CliTask.VERSION:
            writer.write(__version__)
            writer.write("\n")
            return 0

        writer.write(self._parser.format_help())
        return 1
