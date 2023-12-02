FROM brunneis/python:3.7.7-ubuntu-20.04

ARG ALGORITHM_FOLDER=/rgb-footprint-extract

WORKDIR $ALGORITHM_FOLDER

RUN apt-get update \ 
    && apt-get install -y gcc \
    && pip install Cython \
    && pip install numpy==1.18.1 \
    && pip install pycocotools==2.0.0

COPY $ALGORITHM_FOLDER/requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY $ALGORITHM_FOLDER .

COPY ./common ./common

ENTRYPOINT ["python", "run.py"]
