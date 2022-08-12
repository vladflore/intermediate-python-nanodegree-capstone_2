"""This module contains the implementation of the text documents ingestor."""
from typing import List

from .exceptions import UnsupportedQuotesSource
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class TxtIngestor(IngestorInterface):
    """Define the implementation of the ingestor."""

    supported_extensions: List[str] = ['txt']

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
        with open(path) as infile:
            return [cls._createQuote(line) for line in infile.readlines()]

    @classmethod
    def _createQuote(cls, line: str) -> QuoteModel:
        """Create a quote."""
        body, author = line.split('-')
        return QuoteModel(body.strip(), author.strip())
