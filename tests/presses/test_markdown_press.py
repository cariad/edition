from io import StringIO

from comprehemd import read_outline

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


def test__table_of_contents() -> None:
    body = """# one

<edition value="toc" />

## two
"""
    metadata = Metadata(toc=read_outline(StringIO(body)))

    writer = StringIO()
    press = MarkdownPress(
        markdown_body=body,
        metadata=metadata,
    )
    press.press(writer)
    assert (
        writer.getvalue()
        == """# one

- [one](#one)
  - [two](#two)

## two
"""
    )
