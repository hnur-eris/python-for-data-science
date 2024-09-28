from PIL import Image
from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def draw_image(img):
    """
        Displays the given image in grayscale and
        prints its shape and pixel values.
    """
    img = img.convert("L")
    w, h = img.size
    print(f"The shape after slicing:  ({h}, {w}, {len(img.getbands())})",
          f"or ({h}, {w})")
    print(np.array(img))
    # img.show()
    plt.imshow(img, cmap="gray")
    plt.axis("on")
    plt.show()


def main():
    """
    Main function to load an image, crop it and display the result.
    """
    try:
        print(ft_load("animal.jpeg"))
        img = Image.open("animal.jpeg")
        new_img = img.crop(box=(450, 100, 850, 500))
        draw_image(new_img)
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
