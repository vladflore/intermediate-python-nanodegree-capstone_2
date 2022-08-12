"""Define a generic ingestor to be used for ingesting different documents."""
from typing import List

from .csv_ingestor import CsvIngestor
from .docx_ingestor import DocxIngestor
from .ingestor_interface import IngestorInterface
from .pdf_ingestor import PdfIngestor
from .quote_model import QuoteModel
from .txt_ingestor import TxtIngestor


class Ingestor(IngestorInterface):
    """Define the generic ingestor."""

    ingestors: List[IngestorInterface] = [
        TxtIngestor, CsvIngestor, DocxIngestor, PdfIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Define the generic method to be used for parsing documents.

        The concrete ingestors are defined in the `ingestors` attribute.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        return []
