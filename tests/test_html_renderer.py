from io import StringIO

from edition.html_renderer import HtmlRenderer


def test() -> None:
    writer = StringIO()
    HtmlRenderer().render(writer)
    assert writer.getvalue().startswith("<!doctype html>")
