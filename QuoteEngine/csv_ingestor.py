"""This module contains the implementation of the csv documents ingestor."""
from typing import List

import pandas

from .exceptions import UnsupportedQuotesSource
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class CsvIngestor(IngestorInterface):
    """Define the implementation of the ingestor."""

    supported_extensions: List[str] = ['csv']

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
        df = pandas.read_csv(path, header=0)
        return [
            QuoteModel(row['body'], row['author']) for _, row in df.iterrows()
        ]
