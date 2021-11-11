from html.parser import HTMLParser
from importlib.resources import open_text
from sys import stdout
from typing import IO, List, Optional, Tuple

TAttribute = Tuple[str, Optional[str]]


class HtmlRenderer(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._writer: IO[str] = stdout

    def handle_decl(self, decl: str) -> None:
        self._writer.write(f"<!{decl}>")

    def handle_endtag(self, tag: str) -> None:
        self._writer.write(f"</{tag}>")

    def handle_startendtag(self, tag: str, attrs: List[TAttribute]) -> None:
        attributes = self.make_attributes(attrs) if attrs else ""
        inner = f"{tag} {attributes}".strip()
        self._writer.write(f"<{inner} />")

    def handle_starttag(self, tag: str, attrs: Optional[List[TAttribute]]) -> None:
        attributes = self.make_attributes(attrs) if attrs else ""
        inner = f"{tag} {attributes}".strip()
        self._writer.write(f"<{inner}>")

    @staticmethod
    def make_attribute(attribute: TAttribute) -> str:
        return f'{attribute[0]}="{attribute[1]}"'

    @staticmethod
    def make_attributes(attributes: List[TAttribute]) -> str:
        return " ".join([HtmlRenderer.make_attribute(a) for a in attributes])

    def render(self, writer: IO[str]) -> None:
        self._writer = writer
        with open_text(__package__, "document.html") as f:
            self.feed(f.read())
            self.close()
