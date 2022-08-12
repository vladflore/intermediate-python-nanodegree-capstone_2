"""This module contains the implementation of the pdf documents ingestor."""
import os
import random
import subprocess
import tempfile
from typing import List

from .exceptions import UnsupportedQuotesSource
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class PdfIngestor(IngestorInterface):
    """Define the implementation of the ingestor."""

    supported_extensions: List[str] = ['pdf']

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

        tmp = f'{tempfile.gettempdir()}/{random.randint(0,1000000)}.txt'
        call = subprocess.call(
            ['pdftotext', path, tmp])

        file_ref = open(tmp, "r")
        quotes = []
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split('-')
                new_quote = QuoteModel(
                    parsed[0].strip().strip('"'), parsed[1].strip().strip('"'))
                quotes.append(new_quote)

        file_ref.close()
        os.remove(tmp)
        return quotes
