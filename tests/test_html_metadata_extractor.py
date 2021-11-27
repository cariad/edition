# from pytest import mark, raises

# from edition.html_metadata_extractor import HtmlMetadataExtractor
# from edition.metadata import Metadata


# def test_title() -> None:
#     html = """
# <html>
#   <body>
#     <h1>Hello, World?</h1>
#     <p>Something, something.</p>
#   </body>
# </html>
# """
#     metadata = Metadata()
#     HtmlMetadataExtractor(html=html, metadata=metadata).append_metadata()
#     assert metadata.get("title", None) == "Hello, World?"


# @mark.parametrize(
#     "html, expect",
#     [
#         (
#             "<h2>foo</h2>",
#             '<nav class="toc"><ol><li><a href="#foo">foo</a></li></ol></nav>',
#         ),
#         (
#             "<h2><code>foo</code></h2>",
#             '<nav class="toc"><ol><li><a href="#foo"><code>foo</code></a></li></ol></nav>',
#         ),
#     ],
# )
# def test_heading_with_code_in_toc(html: str, expect: str) -> None:
#     metadata = Metadata()
#     HtmlMetadataExtractor(html=html, metadata=metadata).append_metadata()
#     assert metadata.get("toc", None) == expect


# def test_handle_endtag() -> None:
#     extractor = HtmlMetadataExtractor(
#         html="<foo><bar></foo>",
#         metadata=Metadata(),
#     )
#     with raises(ValueError) as ex:
#         extractor.append_metadata()
#     assert str(ex.value) == 'expected to end "bar" but got "foo"'
