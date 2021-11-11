from abc import ABC, abstractmethod
from typing import IO

from edition.metadata import Metadata


class Press(ABC):
    def __init__(self, markdown_body: str, metadata: Metadata) -> None:
        self._markdown_body = markdown_body
        self._metadata = metadata

    @abstractmethod
    def press(self, writer: IO[str]) -> None:
        """Perform the press."""
