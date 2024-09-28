from PIL import Image
import sys
from pynput import keyboard
from load_image import ft_load
import matplotlib.pyplot as plt


class ImageZoomer:
    """
        A class to handle image zooming functionality.
    """
    def __init__(self, image_path):
        """
            Initializes the ImageZoomer with the image at the given path.
        """
        self.img = Image.open(image_path)
        self.zoom_factor = 1.0

    def zoom_image(self):
        """
            Resizes the image according to the
            current zoom factor and returns an image
        """
        new_size = (int(self.img.size[0] * self.zoom_factor),
                    int(self.img.size[1] * self.zoom_factor))
        resized_image = self.img.resize(new_size)
        return resized_image

    def on_press(self, key):
        """
            Handles key press events for zooming in and out.
        """
        try:
            if key.char == '+':
                self.zoom_factor += 0.1
            elif key.char == '-':
                self.zoom_factor -= 0.1
        except KeyboardInterrupt:
            # If pressing special key such as Ctrl + or escape
            if key == keyboard.Key.esc:
                sys.exit()
            elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                sys.exit()


def main():
    """
        Main function to run the image zooming application.

        Initializes the ImageZoomer with a specified image,
        starts the keyboard listener for zooming controls,
        and continuously updates and displays the zoomed image.
    """
    zoomer = ImageZoomer("animal.jpeg")

    with keyboard.Listener(on_press=zoomer.on_press) as listener:
        while listener.running:
            resized_img = zoomer.zoom_image()
            # resized_img.show()
            plt.imshow(resized_img)
            plt.axis('on')  # showing axis on the image
            plt.show(block=False)
            plt.pause(0.1)
            resized_img.save("zoomed.jpg")
            print("pixel of zoomed image: ", ft_load("zoomed.jpg"))


if __name__ == "__main__":
    main()
