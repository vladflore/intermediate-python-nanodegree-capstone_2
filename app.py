"""This module defines the web API to interact with."""
import os
import random

import requests
from flask import Flask, abort, render_template, request

from MemeGenerator import MemeGenerator, MemeLoader
from QuoteEngine import QuotesLoader

app = Flask(__name__)

meme = MemeGenerator('./static')


def setup():
    """Load all resources(quote files and images)."""
    quotes = QuotesLoader.load_quotes()
    imgs = MemeLoader.load_images()

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form.get('image_url')
    quote_body = request.form.get('body', '')
    quote_author = request.form.get('author', '')

    if image_url:
        response = requests.get(image_url)
        ext = image_url.split('.')[-1]
        temp_file = f'./static/{random.randint(0, 10**8)}.{ext}'
        with open(temp_file, 'wb') as img:
            img.write(response.content)
        path = meme.make_meme(temp_file, quote_body, quote_author)
        os.remove(temp_file)
        return render_template('meme.html', path='#' if not path else path)

    return render_template('meme.html', path='#')


if __name__ == "__main__":
    app.run()
