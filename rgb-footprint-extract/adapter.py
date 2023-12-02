from PIL import Image
import numpy as np
import os

class Adapter:

    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        
    def save_image_as_npy(self, filename):
        path_to_file = self.input_path + filename
        image = Image.open(path_to_file).convert('RGB')
        output_path = f'{self.output_path}{filename}.npy'
        if not os.path.isdir(self.output_path):
            os.makedirs(self.output_path)
        np.save(output_path, image)
    
    def convert_images_in_dir(self):
        for file in os.listdir(self.input_path):
            self.save_image_as_npy(file)

    def run(self):
        self.convert_images_in_dir()