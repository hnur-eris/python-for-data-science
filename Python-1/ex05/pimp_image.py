from PIL import Image
import numpy as np


def ft_invert(array) -> np.array:
    """
        Inverts the color values of the image received.
    """
    print(array)
    Image.fromarray(array).show()
    Image.fromarray(255 - array).show()
    return 255 - array


def ft_red(array) -> np.array:
    """
        Inverts the red color values of the image received.
    """
    red = array.copy()
    red[:, :, 1] = 0
    red[:, :, 2] = 0
    Image.fromarray(red).show()
    return red


def ft_green(array) -> np.array:
    """
        Inverts the green color values of the image received.
    """
    green = array.copy()
    green[:, :, 0] = 0
    green[:, :, 2] = 0
    Image.fromarray(green).show()
    return green


def ft_blue(array) -> np.array:
    """
        Inverts the blue color values of the image received.
    """
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    Image.fromarray(blue).show()
    return blue


def ft_grey(array) -> np.array:
    """
        Converts the image to grayscale.
    """
    img = Image.fromarray(array)
    img = img.convert("L")
    img.show()
    return np.array(img)
