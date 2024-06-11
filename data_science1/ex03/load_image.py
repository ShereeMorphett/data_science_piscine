from PIL import Image
import numpy as np

# You need to write a function that loads an image, prints its format, and its pixels
# content in RGB format.
# You have to handle, at least, JPG and JPEG format.
# You need to handle any error with a clear error message

def ft_load(path: str) -> np.ndarray:
    """_summary_
    Loads an image, prints the shape of the image and returns an array
    Args:
        path (str): image file path

    Returns:
        np.ndarray: the RGB pixel matrix in numpy array"""    
    try:
        image = Image.open(path)
        im_array = np.array(image)
        print(im_array.shape)
        return(im_array)
    except Exception as e:
        print(f"Error: {e}")



def main():
    """_summary_
        This is a main, it simply calls 
    """    
    ft_load("landscape.jpg")



if __name__ == "__main__":
    main()
