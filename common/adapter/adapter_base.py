from pathlib import Path
from abc import ABC, abstractmethod

class AdapterBase(ABC):

    def __init__(self, input_path : Path, output_path : Path):
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