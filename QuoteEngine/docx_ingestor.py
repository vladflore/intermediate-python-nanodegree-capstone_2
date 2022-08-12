"""This module contains the implementation of the docx documents ingestor."""
from typing import List

import docx

from .exceptions import UnsupportedQuotesSource
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class DocxIngestor(IngestorInterface):
    """Define the implementation of the ingestor."""

    supported_extensions: List[str] = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Define the parse algorithm.

        Arguments:
        path -- the path to the document to ingest

        Return:
        a list of `QuoteModel` objects
        """
        if not cls.can_ingest(path):
            raise UnsupportedQuotesSource(
                f'Cannot ingest quotes document: {path}.')

        doc = docx.Document(path)
        return [
            cls._create_quote(paragraph.text)
            for paragraph in doc.paragraphs if paragraph.text != ""
        ]

    @classmethod
    def _create_quote(cls, line: str) -> QuoteModel:
        """Create a quote."""
        body, author = line.split('-')
        return QuoteModel(body.strip().strip('"'), author.strip().strip('"'))
