"""This module is responsible with generating a new meme.

It can also be used as a CLI tool.
"""
import argparse
import random

from MemeGenerator import MemeGenerator, MemeLoader
from QuoteEngine import InvalidQuote, QuoteModel, QuotesLoader


def generate_meme(path=None, body=None, author=None) -> str:
    """Generate a meme.

    Keyword arguments:
    path -- the path to the image. If none provided a random one is chosen.
        If more, a random one amongst those is chosen.
    body -- the meme's text. If none provided a random one
        (together with the author) is chosen.
    author -- the meme's author. If none provided and body is given
        an exception is raised.

    Return:
    the path to the generated image, might be `None`
    """
    img = None
    quote = None

    if path is None:
        imgs = MemeLoader.load_images()
        img = random.choice(imgs)
    else:
        img = random.choice(path)

    if body is None:
        quotes = QuotesLoader.load_quotes()
        quote = random.choice(quotes)
    else:
        if author is None:
            raise InvalidQuote('Author required if body is used.')
        quote = QuoteModel(body, author)

    meme = MemeGenerator('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Adds text to a picture.')
    parser.add_argument('-p', '--path', nargs='+',
                        help=('One or more(separated by space) image paths. '
                              'If multiple images are given, a random '
                              'one is chosen. Not required.'))
    parser.add_argument('-b', '--body', help='The meme\'s text. Not required.')
    parser.add_argument(
        '-a', '--author', help='The author of the meme. Not required.')
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
