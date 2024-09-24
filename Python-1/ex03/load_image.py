from PIL import Image
import numpy as np
from numpy import array
import os


def error_handle(path: str):
    assert not path.endswith(("jpg", "jpeg")), "Doesn't match expected format"
    assert not os.path.exists(path), "File doesn't found"


def ft_load(path: str) -> array:
    try:
        error_handle(path)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit()
    im = Image.open(path)
    width, height = im.size
    print(f"The shape of image is ({height}, {width}, {len(im.getbands())})")
    return np.array(im)
