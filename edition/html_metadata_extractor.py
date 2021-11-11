from html.parser import HTMLParser
from typing import List, Optional, Tuple

from edition.metadata import Metadata

TAttribute = Tuple[str, Optional[str]]


class HtmlMetadataExtractor(HTMLParser):
    def __init__(self, html: str, metadata: Metadata) -> None:
        super().__init__()
        self._html = html
        self._metadata = metadata
        self._path: List[str] = []

    def append_metadata(self) -> None:
        self.feed(self._html)
        self.close()

    def handle_data(self, data: str) -> None:
        if self._path and self._path[-1].lower() == "h1":
            self._metadata["title"] = self._metadata.get("title", data.strip())

    def handle_endtag(self, tag: str) -> None:
        popped = self._path.pop()
        if popped != tag:
            raise ValueError(f'expected to end "{popped}" but got "{tag}"')

    def handle_starttag(self, tag: str, attrs: Optional[List[TAttribute]]) -> None:
        self._path.append(tag)
