from io import StringIO

from edition.html_renderer import EditionHtmlRenderer


def test() -> None:
    writer = StringIO()
    EditionHtmlRenderer().render(feed="<!doctype html>", writer=writer)
    assert writer.getvalue().startswith("<!doctype html>")
