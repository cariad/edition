from io import StringIO

from edition.edition import Edition


def test() -> None:
    edition = Edition(
        """
# Hello!

This is just some _Markdown_.
"""
    )

    writer = StringIO()
    edition.press(writer)
    assert writer.getvalue().startswith("<!doctype html")
