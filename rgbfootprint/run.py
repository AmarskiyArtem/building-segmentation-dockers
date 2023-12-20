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
    parser.add_argument(
        "--window-size",
        type=int,
        default=None,
        help="the size of grid blocks to sample from the input, use if encountering OOM issues",
    )
    parser.add_argument(
        "--stride",
        type=int,
        default=None,
        help="the stride at which to sample grid blocks, recommended value is equal to `window_size`",
    )
    parser.add_argument(
        "--no-cuda", action="store_true", default=False, help="disables CUDA training"
    )
    parser.add_argument(
        "--gpu-ids", type=str, default="0", help="use which gpu to train, must be a \
                        comma-separated list of integers only (default=0)"
    )
    parser.add_argument(
        "--backbone",
        type=str,
        default="drn_c42",
        choices=["resnet", "xception", "drn", "mobilenet", "drn_c42"],
        help="backbone name (default: resnet)",
    )
    parser.add_argument(
        "--out-stride", type=int, default=8, help="network output stride (default: 8)"
    )
    parser.add_argument(
        "--resume",
        type=str,
        default="crowdAI",
        help="experiment to load (default: crowdAI)",
    )
    args = parser.parse_args()
    adapter.Adapter(args.input_path, args.output_path, args).run()
