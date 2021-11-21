from io import StringIO

from edition.pre_html_renderer import PreHtmlRenderer


def test_code_in_heading() -> None:
    writer = StringIO()
    PreHtmlRenderer().render(
        body="<body><h2><code>foo</code></h2></body>",
        writer=writer,
    )
    assert writer.getvalue() == '<body><h2><code>foo</code><a id="foo"></a></h2></body>'
