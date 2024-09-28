from PIL import Image
import numpy as np
from numpy import array
import os


def error_handle(path: str):
    """
        Checks if the given file path is valid.
    """
    assert path.endswith(("jpg", "jpeg")), "Doesn't match expected format"
    assert os.path.exists(path), "File doesn't found"


def ft_load(path: str) -> array:
    """
        Loads an image from the specified
        file path and converts it to a NumPy array.
    """
    try:
        error_handle(path)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit()
    im = Image.open(path)
    width, height = im.size
    print(f"The shape of image is ({height}, {width}, {len(im.getbands())})")
    return np.array(im)
