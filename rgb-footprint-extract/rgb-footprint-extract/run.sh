#!/bin/bash

input_path="$1"
output_path="$2"

for file in "$input_path"*; do
  if [ -f "$file" ]; then
  filename=$(basename "$file")
  filename_no_extension=${filename%.*}
    python3 ./rgb-footprint-extract/run_deeplab.py --inference --backbone=drn_c42 --out-stride=8 --workers=2 --epochs=1 --test-batch-size=1 --no-cuda --resume=crowdAI --best-miou --input-filename="$file"    --output-filename="$output_path$filename_no_extension.png"
  fi
done
