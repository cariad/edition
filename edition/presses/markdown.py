from typing import IO

from edition.presses.press import Press


class MarkdownPress(Press):
    def press(self, writer: IO[str]) -> None:
        # TODO: dinject md_body
        writer.write(self._markdown_body)
