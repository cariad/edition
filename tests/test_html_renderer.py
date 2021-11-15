from io import StringIO

from edition.html_renderer import EditionHtmlRenderer


def test_handle_comment() -> None:
    reader = StringIO("<!--foo-->")
    writer = StringIO()
    EditionHtmlRenderer().render(reader=reader, writer=writer)
    assert writer.getvalue() == "&lt;!--foo--&gt;"
