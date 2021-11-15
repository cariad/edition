from pytest import mark

from edition.html import get_css, get_html_template, to_anchor_id


@mark.parametrize(
    "text, expect",
    [
        ("foo", "foo"),
        ("Foo", "foo"),
        ("foo bar", "foo-bar"),
        ("🍕 pizza", "-pizza"),
    ],
)
def test_to_anchor_id(text: str, expect: str) -> None:
    assert to_anchor_id(text) == expect


def test_get_css() -> None:
    with get_css() as f:
        actual = f.read()
    assert actual.startswith("body {")
    assert actual.endswith("margin-bottom: 1rem;\n}\n")


def test_get_html_template() -> None:
    with get_html_template() as f:
        actual = f.read()
    assert actual.startswith("<!doctype html>")
    assert actual.endswith("</html>\n")
