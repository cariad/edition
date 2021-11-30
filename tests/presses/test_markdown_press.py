from io import StringIO

from edition import Metadata
from edition.presses import MarkdownPress


def test() -> None:
    writer = StringIO()
    press = MarkdownPress(
        markdown_body="""# Hello!

This is just some _Markdown_.
""",
        metadata=Metadata(),
    )
    press.press(writer)
    assert writer.getvalue().startswith("# Hello!")


def test__do_not_escape_html_comments() -> None:
    writer = StringIO()
    press = MarkdownPress(
        markdown_body="For example, `<!--foo-->`.",
        metadata=Metadata(),
    )
    press.press(writer)
    assert writer.getvalue() == "For example, `<!--foo-->`.\n"
