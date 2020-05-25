"""
This program implements a rad image filter.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.jpg'

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)
    new_image = SimpleImage.blank(900,559)

    # Show the image before the transform
    image.show()
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x,y)
            pixel.red = pixel.red * 1.5
            pixel.green = pixel.green * 0.7
            pixel.blue = pixel.blue * 1.5
            new_image.set_pixel(x,y,pixel)
    new_image.show()



    # Apply the filter
    # TODO: your code here

    # Show the image after the transform
    #image.show()


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()