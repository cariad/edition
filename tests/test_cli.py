from io import StringIO

from edition.cli import Cli, CliTask


def test_invoke__make() -> None:
    writer = StringIO()
    assert Cli(["docs/src.md", "--press", "html"]).invoke(writer) == 0
    assert writer.getvalue().startswith("<!doctype html>")


def test_invoke__none() -> None:
    writer = StringIO()
    assert Cli([]).invoke(writer) == 1
    assert writer.getvalue().startswith("usage:")


def test_invoke__version() -> None:
    writer = StringIO()
    assert Cli(["--version"]).invoke(writer) == 0
    assert writer.getvalue() == "-1.-1.-1\n"


def test_parse__make() -> None:
    assert Cli(["docs/src.md", "--press", "html"]).task == CliTask.MAKE


def test_parse__none() -> None:
    assert Cli([]).task == CliTask.HELP


def test_parse__version() -> None:
    assert Cli(["--version"]).task == CliTask.VERSION
