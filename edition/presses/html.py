from typing import IO

from markdown import markdown

from edition.html_metadata_extractor import HtmlMetadataExtractor
from edition.html_renderer import HtmlRenderer
from edition.presses.press import Press


class HtmlPress(Press):
    def press(self, writer: IO[str]) -> None:
        html_body = markdown(self._markdown_body, output_format="html")
        HtmlMetadataExtractor(html_body, self._metadata).append_metadata()
        HtmlRenderer().render(writer)
