from io import StringIO

from edition import Metadata
from edition.presses import HtmlPress


def test() -> None:
    writer = StringIO()
    press = HtmlPress(
        markdown_body="""
# Hello!

This is just some _Markdown_.
""",
        metadata=Metadata(),
    )
    press.press(writer)
    assert writer.getvalue().startswith("<!doctype html")
