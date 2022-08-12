"""Define the common interface of the different document ingestors."""
from abc import ABC, abstractmethod
from typing import List

from .quote_model import QuoteModel


class IngestorInterface(ABC):
    """Define the ingestor interface as an abstract class."""

    supported_extensions: List[str] = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Determine if the concrete ingestor can ingest specific documents."""
        extension = path.split('.')[-1]
        return extension in cls.supported_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Define an abstract method to be implemented by actual ingestors."""
        pass
