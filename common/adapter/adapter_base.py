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

from abc import ABC, abstractmethod
from argparse import ArgumentParser
from pathlib import Path


class AdapterBase(ABC):
    def __init__(self, input_path: Path, output_path: Path, args: ArgumentParser):
        self.input_path = input_path
        self.output_path = output_path

    @abstractmethod
    def preprocessing(self):
        pass

    @abstractmethod
    def convert_to_input_format(self):
        pass

    @abstractmethod
    def predict_masks(self):
        pass

    @abstractmethod
    def convert_to_output_format(self):
        pass

    @abstractmethod
    def postprocessing(self):
        pass

    def run(self):
        self.preprocessing()
        self.convert_to_input_format()
        self.predict_masks()
        self.convert_to_output_format()
        self.postprocessing()
