# Implimentation of YoloV5 with DeepSORT

## Prepare

### Environments

- Python 3.8.16

Install libraries

``` bash
pip install -U pip --no-cache-dir
git clone https://github.com/ultralytics/yolov5
pip install -r yolov5/requirements.txt
pip install -r requirements.txt
```

### Pretrained weights

- Download DeepSORT weights from [here](https://drive.google.com/file/d/1x1NJwotZso1LeRA_I6VR1Tzl02gYL6dR/view?usp=sharing) to `./deep_sort/deep/checkpoint` or run

``` bash
gdown https://drive.google.com/uc?id=1x1NJwotZso1LeRA_I6VR1Tzl02gYL6dR -O ./deep_sort/deep/checkpoint/ckpt.t7
```

- Yolo pretrained weight is auto downloaded when you run for the first time

## Run

Run program with

``` bash
python main.py --input_path /media/mera/Mera/AI/DATN/video/capture_0.avi --display --classes 2 3 5 6 7
```

## Reference

- [HowieMa/DeepSORT_YOLOv5_Pytorch](https://github.com/HowieMa/DeepSORT_YOLOv5_Pytorch)