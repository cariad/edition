from io import StringIO

from edition.html_renderer import EditionHtmlRenderer


def test() -> None:
    writer = StringIO()
    EditionHtmlRenderer().render(writer)
    assert writer.getvalue().startswith("<!doctype html>")
