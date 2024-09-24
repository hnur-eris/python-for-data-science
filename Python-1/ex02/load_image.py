from PIL import Image
import numpy as np
from numpy import array
import os


def ft_load(path: str) -> array:
    try:
        assert not path.endswith(("jpg", "jpeg")), "The file \
            xtension does not match the expected \
                format such as JPG or JPEG"
        assert not os.path.exists(path), "File doesn't found"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit()
    im = Image.open(path)
    im_arr = np.array(im)
    width, height = im.size
    print(f"The shape of image is ({height}, {width}, \
        {len(im.getbands())})")
    return im_arr
