"""This module contains the model for a quote."""


class QuoteModel():
    """Define the model for a quote."""

    def __init__(self, body: str, author: str) -> None:
        """Initialize a quote object.

        A quote contains a `body` and an `author`.

        Arguments:
        `body` -- the text of the quote, as a `str`
        `author` -- the author of the quote, as a `str`
        """
        self.body = body
        self.author = author

    def __repr__(self) -> str:
        """Return a computer-readable string representation of this object."""
        return f'"{self.body}" - {self.author}'

    def __str__(self) -> str:
        """Return a human-readable string representation of this object."""
        return f'"{self.body}" - {self.author}'
