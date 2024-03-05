import os
import random
import matplotlib.image as mpimg
import numpy as np


def get_image_and_class(train_folder: str) -> tuple[np.ndarray, str]:
    """
    Selects a random image from a specified folder and its class name.

    Args:
        folder (str): Path to the folder containing class subfolders with images.

    Returns:
        tuple[np.ndarray, str]: A tuple containing the normalized image as a NumPy array and the class name (subfolder name).

    Example usage:
        img, class_name = get_random_image_and_class("./data/train")
    """
    class_name = random.choice(os.listdir(train_folder))
    target_path = os.path.join(train_folder, class_name + "/")
    target_img = random.choice(os.listdir(target_path))
    path = os.path.join(train_folder, class_name, target_img)
    img = mpimg.imread(path)
    img = img / 255.0
    return img, class_name
