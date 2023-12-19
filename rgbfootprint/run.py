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

import argparse
import adapter

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-path",
        type=str,
        help="Path to the images",
        default="/rgbfootprint/rgb_footprint_extract/input",
    )
    
    parser.add_argument(
        "--output-path", 
        type=str,
        help="Path to the segmentation masks",
        default="/rgbfootprint/rgb_footprint_extract/output",
    )  

    args = parser.parse_args()
    adapter.Adapter(
        input_path=args.input_path,
        output_path=args.output_path
    ).run()