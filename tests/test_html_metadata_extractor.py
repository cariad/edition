from pytest import raises

from edition.html_metadata_extractor import HtmlMetadataExtractor
from edition.metadata import Metadata


def test_title() -> None:
    html = """
<html>
  <body>
    <h1>Hello, World?</h1>
    <p>Something, something.</p>
  </body>
</html>
"""
    metadata = Metadata()
    HtmlMetadataExtractor(html=html, metadata=metadata).append_metadata()
    assert metadata.get("title", None) == "Hello, World?"


def test_handle_endtag() -> None:
    extractor = HtmlMetadataExtractor(
        html="<foo><bar></foo>",
        metadata=Metadata(),
    )
    with raises(ValueError) as ex:
        extractor.append_metadata()
    assert str(ex.value) == 'expected to end "bar" but got "foo"'
