from PIL import Image
import numpy as np
import os

def save_image_as_npy(path_to_file, path_to_output_dir):
    filename, file_extension = os.path.splitext(os.path.basename(path_to_file))
    image = Image.open(path_to_file).convert('RGB')
    output_path = f'{path_to_output_dir}{filename}.npy'
    if not os.path.isdir(path_to_output_dir):
        os.makedirs(path_to_output_dir)
    np.save(output_path, image)

def convert_images_in_dir(path_to_input_dir, path_to_output_dir):
    for file in os.listdir(path_to_input_dir):
        save_image_as_npy(path_to_input_dir + file, path_to_output_dir)