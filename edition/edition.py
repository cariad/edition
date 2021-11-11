from typing import IO, Tuple, cast

import frontmatter  # pyright: reportMissingTypeStubs=false
from markdown import markdown

from edition.html_metadata_extractor import HtmlMetadataExtractor
from edition.html_renderer import HtmlRenderer
from edition.metadata import Metadata


class Edition:
    def __init__(self, markdown: str) -> None:
        self._markdown = markdown

    def press(self, writer: IO[str]) -> None:
        metadata, md_body = cast(
            Tuple[Metadata, str],
            frontmatter.parse(self._markdown),
        )  # pyright: reportUnknownMemberType=false

        html_body = markdown(md_body, output_format="html")
        HtmlMetadataExtractor(html_body, metadata).append_metadata()
        HtmlRenderer().render(writer)
