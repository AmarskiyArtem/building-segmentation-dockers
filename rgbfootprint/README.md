## RGB-footprint-extract Docker Image

The folder contains adapter and docker image for [A Semantic Segmentation Network for Urban-Scale Building Footprint
Extraction Using RGB Satellite Imagery](https://github.com/aatifjiwani/rgb-footprint-extract)

## Installation
Clone the repo. Use git LFS to download model weights.

```
https://github.com/AmarskiyArtem/building-segmentation-dockers.git
cd rgb-footprint-extract
```
## Building Docker Image

```
docker build -t rgbfootprint -f Dockerfile ..
```

## Running method

```
docker run --rm \
-v <IMAGES_PATH>:/rgbfootprint/rgb-footprint-extract/input \
-v <OUTPUT_PATH>:/rgbfootprint/rgb-footprint-extract/output \
rgbfootprint [OPTIONAL_ARGS]
```

Here `<IMAGES_PATH>` should be the path to the folder with images to prediction, `<OUTPUT_PATH>` is the path where the predicted masks will be saved.

The following `[OPTIONAL_ARGS]` can be used:

optional arguments:
| Parameter             | Default| Description (final argument) |	
| :--------------------:|:------:| :----------------------------|
| &#8209;&#8209;input_path | `/rgbfootprint/rgb-footprint-extract/input` | Path to the images
| &#8209;&#8209;output_path| `/rgbfootprint/rgb-footprint-extract/output` | Path to the masks
| &#8209;&#8209;backbone |	`drn_c42` | The DeeplabV3+ backbone **(final method used `drn_c42`)**
| &#8209;&#8209;out-stride | 8 | The backbone compression facter **(8)**
| &#8209;&#8209;gpu-ids | `0` | GPU Ids (Use `--no-cuda` for only CPU)
| &#8209;&#8209;checkname | None | Experiment name
| &#8209;&#8209;use-wandb | False | Track experiment using WandB
| &#8209;&#8209;resume | crowdAI | Experiment name to load weights from (i.e. `urban` for `weights/urban/checkpoint.pth.tar`)
