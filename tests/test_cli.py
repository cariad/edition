from typing import List

from cline import AnyTaskType
from pytest import mark

import edition.tasks
from edition.cli import Cli


@mark.parametrize(
    "args, expect",
    [
        (["foo", "bar", "--press", "html"], edition.tasks.PressTask),
        (["foo", "bar", "--press", "markdown"], edition.tasks.PressTask),
    ],
)
def test_task(args: List[str], expect: AnyTaskType) -> None:
    cli = Cli(args=args)
    assert isinstance(cli.task, expect)
