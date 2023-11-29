import numpy as np
from abc import ABC, abstractmethod

class AdapterBase(ABC):

    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir

    def run(self):
        self._convert_to_input_format()