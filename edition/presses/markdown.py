from io import StringIO
from typing import IO

from comprehemd import MarkdownParser
from dinject.enums import Content, Host
from dinject.types import ParserOptions

from edition.html_renderer import EditionHtmlRenderer
from edition.presses.press import Press


class MarkdownPress(Press):
    @property
    def injection_options(self) -> ParserOptions:
        return ParserOptions(force_content=Content.MARKDOWN, force_host=Host.SHELL)

    def _press(self, writer: IO[str]) -> None:
        # First, find and expand <edition.../> tags.

        reader = StringIO(self._markdown_body)
        toc = self._metadata.get("toc", None)

        for block in MarkdownParser().read(reader):
            # Ask EditionHtmlRenderer to check for and handle any <edition.../>
            # tag in this block.
            renderer = EditionHtmlRenderer(
                metadata=self._metadata,
                toc_writer=toc.render if toc else None,
            )

            renderer.render(
                reader=block.source,
                writer=writer,
            )
            writer.write("\n")
