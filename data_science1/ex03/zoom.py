from load_image import ft_load
from PIL import Image, ImageOps
import numpy as np

# Create a program that should load the image "animal.jpeg", print some information
# about it and display it after "zooming".
# • The size in pixel on both X and Y axis
# • The number of channel
# • The pixel content of the image.
# If anything went wrong, the program must not stop abruptly and handle any error
# with a clear message.


def main():
    """_summary_
        This is a main, it simply calls 
    """    
    try:
        pic = ft_load("animal.jpeg")
        height = pic.shape[0]
        print(pic)

        left = 400
        top = 176
        right = 800
        bottom = 3 * height / 4

        image2 = Image.fromarray(pic)
        image2 = image2.crop((left, top, right, bottom))
        image2 = ImageOps.grayscale(image2)
        image2 = image2.resize((400,400))

        data = np.array(image2)

        print(data.shape)
        print(data)
        # Shows the image in image viewer 
        image2.show()
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
