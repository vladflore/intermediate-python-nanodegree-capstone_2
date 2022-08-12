"""This module defines a meme generator."""
import os

from PIL import Image, ImageDraw, ImageFont, UnidentifiedImageError


class MemeGenerator():
    """Define the meme generator."""

    def __init__(self, out_path) -> None:
        """Initialize the meme generator.

        Arguments:
        out_path -- a temporary directory location where image artifacts
            are saved. If the directory does not exist, it is created.
        """
        if not os.path.isdir(out_path):
            os.makedirs(out_path)

        self.out_path = out_path

    def make_meme(self,
                  img_path: str, text: str, author: str, width=500) -> str:
        """Create a meme.

        Arguments:
        img_path -- the image path
        text -- the meme's text to be placed on the image
        author -- the author of the meme to be placed on the image

        Keyword arguments:
        width -- the width of the final image.
                    The height is scaled proportionally

        Returns:
        the location of the new image with the meme on it, or `None` if either
            OSError or ValueError was raised
        """
        out_path = f"{self.out_path}/output_{img_path.split('/')[-1]}"

        try:
            with Image.open(img_path) as img:
                if width is not None:
                    ratio = width/float(img.size[0])
                    height = int(ratio*float(img.size[1]))
                    img = img.resize((width, height), Image.NEAREST)
                if text is not None and author is not None:
                    draw = ImageDraw.Draw(img)
                    font = ImageFont.truetype(
                        './fonts/LilitaOne-Regular.ttf', size=20)
                    sep = ' - ' if len(author) > 0 else ''
                    text = f'{text}{sep}{author}'
                    draw.text((10, 30), text,
                              font=font, fill='white')
                img.save(out_path)
        except (OSError, ValueError):
            out_path = None
        return out_path
