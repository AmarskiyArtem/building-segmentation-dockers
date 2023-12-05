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
from pathlib import Path

from common.adapter.adapter_base import AdapterBase

class Adapter(AdapterBase):

    def __init__(self, input_path, output_path):
        super().__init__(Path(input_path), Path(output_path))
        
    def preprocessing(self):
        pass
    
    def save_image_as_npy(self, file_path : Path, npy_path : Path):
        filename = file_path.stem
        image = Image.open(file_path).convert('RGB')
        output = npy_path.joinpath(f'{filename}.npy')
        if not npy_path.is_dir():
            npy_path.mkdir(parents=True, exist_ok=True)
        np.save(output, image)
    
    def convert_to_input_format(self):
        for file in self.input_path.iterdir():
            if file.suffix in ['.png', '.jpg']:
                self.save_image_as_npy(self.input_path / file, 
                                       self.input_path.parent.joinpath(self.input_path.name + '_npy'))

    def predict_masks(self):
        os.chdir('/rgb-footprint-extract/rgb-footprint-extract/')
        os.system(f'bash run.sh {str(self.input_path)[:-1]}_npy/ {self.output_path}')

    def convert_to_output_format(self):
        pass

    def postprocessing(self):
        pass
