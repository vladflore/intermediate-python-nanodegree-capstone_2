# Motivational Meme Generator

## Overview

This project exposes two ways to generate and visualize memes. A meme is actually an image with a quote applied onto it. First way is as a web application, accessible over an URL, the second, as a CLI tool.

## Prerequisites

### Provide images and quotes

This is an optional step, i.e. a couple of images and quotes(as different files) have already been provided. If you want to use your own images and quote files, add them accordingly under the following locations:

Images location: `_data/photos/dog`

Quotes location: `_data/dog_quotes`

Following quotes files are supported: `txt`,`csv`,`docx`,`pdf`.

Both the image and quote files are automatically discovered once they have been placed directly under their respective locations.

### Install project dependencies

1. Create a virtual environment and activate it

```shell
python3 -m venv myenv
source myenv/bin/activate
```

2. Install project dependencies

```shell
pip install -r requirements.txt
```

## Run

### as a web application

```shell
python3 app.py
```

Open the URL that is shown in the terminal message: `Running on <URL>`.

### as a CLI

The CLI tool can be used in two ways:

1. without any arguments, in which case a random image and quote are used

```shell
python3 main.py
```

This prints a path to the new generated meme (e.g. `./tmp/output_dog1.jpg`)

2. with specific options to control the pool of images and the quote content

Run `python3 main.py -h` to get accustomed with the available options.

Running examples:

- with one image, no quote:

```shell
python3 main.py -p /home/vladflore/pers/intermediate-python-nanodegree/capstone-2/proj/_data/photos/dog/dog5.jpg
```

- with two images, no quote:

```shell
python3 main.py -p /home/vladflore/pers/intermediate-python-nanodegree/capstone-2/proj/_data/photos/dog/dog5.jpg /home/vladflore/pers/intermediate-python-nanodegree/capstone-2/proj/_data/photos/dog/dog4.jpg
```

- with one image and quote (body `-b` and author `-a`):

```shell
python3 main.py -p /home/vladflore/pers/intermediate-python-nanodegree/capstone-2/proj/_data/photos/dog/dog5.jpg -b "Lore ipsum" -a "The Author"
```

Note: providing only the body and no author does not constitute a valid quote and will not be accepted!

## A deeper look

### Project structure

```shell
.
├── app.py              --> contains the Flask-based web app
├── _data               --> contains the image and quotes files
├── fonts               --> contains a text font used for writing on the image
├── main.py             --> contains the CLI tool
├── MemeGenerator       --> contains modules for generating a meme
├── QuoteEngine         --> contains modules for processing quotes
├── README.md           --> this file
├── requirements.txt    --> listing of project dependencies to be installed with `pip`
├── templates           --> HTML templates to display in the browser
```

- the `MemeGenerator` package

```shell
.
├── __init__.py         --> defines the package
├── loader.py           --> loads images from the `_data/photos/dog` folder
├── meme_generator.py   --> generates a new meme(image with a quote on it)
```

- the `QuoteEngine` package

```shell
.
├── csv_ingestor.py         --> the `csv` ingestor
├── docx_ingestor.py        --> the `docx` ingestor
├── exceptions.py           --> custom exceptions relating to processing quotes
├── ingestor_interface.py   --> generic ingestor interface all concrete ingestor have to implement
├── ingestor.py             --> a facade to use the ingestors
├── __init__.py             --> defines the package
├── loader.py               --> loads quotes from the `_data/dog_quotes` folder
├── pdf_ingestor.py         --> the `pdf` ingestor
├── quote_model.py          --> defines the quote Python object to hold the quote data
└── txt_ingestor.py         --> the `txt` ingestor
```

Note: `static`, and `tmp` folders are creating by the application at runtime. `myenv` is the name of the folder containing the Python environment created earlier.
