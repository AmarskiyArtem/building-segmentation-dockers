# Copyright (c) 2023, Artem Amarskiy, Anastasiia Kornilova, Kirill Ivanov
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
import os

from PIL import Image

from common.adapter.adapter_base import AdapterBase

class Adapter(AdapterBase):

    def __init__(self, input_path, output_path):
        super().__init__(input_path, output_path)
        
    def preprocessing(self):
        pass
    
    def save_image_as_npy(self, file, npy_path):
        filename, file_extension = os.path.splitext(os.path.basename(file))
        image = Image.open(self.input_path + file).convert('RGB')
        output = f'{npy_path}{filename}.npy'
        if not os.path.isdir(npy_path):
            os.makedirs(npy_path)
        np.save(output, image)
    
    def convert_to_input_format(self):
        for file in os.listdir(self.input_path):
            self.save_image_as_npy(file, self.input_path[:-1] + '_npy/')

    def predict_masks(self):
        os.chdir('/rgb-footprint-extract/rgb-footprint-extract/')
        os.system(f'bash run.sh {self.input_path[:-1]}_npy/ {self.output_path}/')

    def convert_to_output_format(self):
        pass

    def postprocessing(self):
        pass

    def run(self):
        super().run()
