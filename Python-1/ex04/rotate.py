from PIL import Image
from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def draw_image(img, arr):
    """
        Displays the given image in grayscale and
        prints its shape and pixel values.
    """
    print(f"New shape after Transpose: {img.size}\n{arr}")
    img.show()
    plt.imshow(img, cmap="gray")
    plt.axis("on")
    plt.show()
    # plt.pause(2)


def transpose(matrix):
    """"
        Calculates the transpose of the given matrix
    """
    row = len(matrix)
    col = len(matrix[0])
    transpose = []
    for i in range(col):
        temp = []
        for j in range(row):
            temp.append(matrix[j][i])
        transpose.append(temp)
    return np.array(transpose)


def main():
    """
        Main function to load an image, crop it,
        transpose it and display the result.
    """
    try:
        img = Image.open("animal.jpeg")

        img = img.crop(box=(450, 100, 870, 500))
        img = img.convert("L")

        img.save("crop.jpg")
        arr_img = ft_load("crop.jpg")
        print(arr_img)
        t_arr = transpose(arr_img)
        tr_img = Image.fromarray(t_arr, mode="L")
        draw_image(tr_img, t_arr)

    except KeyboardInterrupt as msg:  # CTRL + C yapınca sıkıntı oluyo
        print(f"Error: {msg}")
        return


if __name__ == "__main__":
    main()
