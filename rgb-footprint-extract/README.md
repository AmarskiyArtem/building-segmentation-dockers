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
docker run --gpus all --rm \
-v <IMAGES_PATH>:/rgb-footprint-extract/rgb-footprint-extract/input \
-v <OUTPUT_PATH>:/rgb-footprint-extract/rgb-footprint-extract/output \
rgbfootprint
```

Here ```<IMAGES_PATH>``` should be the path to the folder with images to prediction, ```<OUTPUT_PATH>``` is the path where the predicted masks will be saved.
