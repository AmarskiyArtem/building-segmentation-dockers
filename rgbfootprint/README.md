## RGB-footprint-extract Docker Image

The folder contains adapter and docker image for [A Semantic Segmentation Network for Urban-Scale Building Footprint
Extraction Using RGB Satellite Imagery](https://github.com/aatifjiwani/rgb-footprint-extract)

## Installation
Clone the repo

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
```
optional arguments:
| Parameter                 | Default       | Description (final argument)  |	
| :------------------------ |:-------------:| :-------------|
| --input_path | /rgbfootprint/rgb-footprint-extract/input | Path to the images
| --output_path | /rgbfootprint/rgb-footprint-extract/output | Path to the masks
| --backbone 	    |	`drn_c42`         | The DeeplabV3+ backbone **(final method used `drn_c42`)**
| --out-stride | 8 | The backbone compression facter **(8)**
| --gpu-ids | `0` | GPU Ids (Use `--no-cuda` for only CPU)
| --checkname | None | Experiment name
| --use-wandb | False | Track experiment using WandB
| --resume | crowdAI | Experiment name to load weights from (i.e. `urban` for `weights/urban/checkpoint.pth.tar`)
```