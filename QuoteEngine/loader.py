"""This module defines a loader class to load quotes."""


import os
from typing import List

from .ingestor import Ingestor
from .quote_model import QuoteModel


class QuotesLoader():
    """Load quotes from a given location."""

    @classmethod
    def load_quotes(cls) -> List[QuoteModel]:
        """Load quotes from given file locations."""
        quotes = []
        quotes_path = f'{os.path.dirname(__file__)}/../_data/dog_quotes/'
        for root, _, files in os.walk(quotes_path):
            for file in files:
                file_ext = file.split('.')[-1]
                if file_ext in ['txt', 'csv', 'docx', 'pdf']:
                    quotes.extend(Ingestor.parse(os.path.join(root, file)))
        return quotes
