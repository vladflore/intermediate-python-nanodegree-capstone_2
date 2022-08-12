"""This module defines a loader class to load images."""


import os
from typing import List


class MemeLoader():
    """Define a loader to load images."""

    @classmethod
    def load_images(cls) -> List[str]:
        """Load images from a given location."""
        imgs = []
        images_path = f'{os.path.dirname(__file__)}/../_data/photos/dog/'
        for root, _, files in os.walk(images_path):
            imgs = [os.path.join(root, file) for file in files]
        return imgs
