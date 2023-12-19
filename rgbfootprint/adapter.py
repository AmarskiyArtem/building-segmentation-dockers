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

from PIL import Image
from pathlib import Path

from rgb_footprint_extract import run_deeplab
from common.adapter.adapter_base import AdapterBase


class Adapter(AdapterBase):
    def __init__(self, input_path, output_path, args):
        self.input_path = Path(input_path)
        self.output_path = Path(output_path)
        self.npy_path = self.input_path.parent.joinpath(self.input_path.name + "_npy")
        self.args = args

    def preprocessing(self):
        pass

    def save_image_as_npy(self, file_path: Path):
        filename = file_path.stem
        image = Image.open(file_path).convert("RGB")
        output = self.npy_path.joinpath(f"{filename}.npy")
        if not self.npy_path.is_dir():
            self.npy_path.mkdir(parents=True, exist_ok=True)
        np.save(output, image)

    def convert_to_input_format(self):
        for file in self.input_path.iterdir():
            if file.suffix in [".png", ".jpg"]:
                self.save_image_as_npy(file)

    def predict_masks(self):
        for file in self.npy_path.iterdir():
            run_deeplab.main(file, self.output_path.joinpath(file.stem + ".png"), self.args)

    def convert_to_output_format(self):
        pass

    def postprocessing(self):
        pass
