"""This module defines exceptions common to the quote engine."""


class UnsupportedQuotesSource(Exception):
    """Define a unsupported quotes source exception."""

    ...


class InvalidQuote(Exception):
    """Define an invalid quote exception."""

    ...
