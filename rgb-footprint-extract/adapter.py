from PIL import Image
import numpy as np
import os

class Adapter:

    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        
    def save_image_as_npy(self, file, npy_path):
        filename, file_extension = os.path.splitext(os.path.basename(file))
        image = Image.open(self.input_path + file).convert('RGB')
        output = f'{npy_path}{filename}.npy'
        if not os.path.isdir(npy_path):
            os.makedirs(npy_path)
        np.save(output, image)
    
    def convert_images_in_dir(self):
        for file in os.listdir(self.input_path):
            self.save_image_as_npy(file, self.input_path[:-1] + '_npy/')

    def run(self):
        self.convert_images_in_dir()
        os.chdir('/rgb-footprint-extract/rgb-footprint-extract/')
        os.system(f'bash run.sh {self.input_path[:-1]}_npy/ {self.output_path}/')
