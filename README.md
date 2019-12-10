# Yolo3
Blood Cell Detection with Yolov3

This code implements yolov3 from papers
1. [YOLOv3: An Incremental Improvement](https://arxiv.org/pdf/1804.02767.pdf)
2. [YOLO9000: Better, Faster, Stronger](https://arxiv.org/pdf/1612.08242.pdf)

The test environment is 
* Python 3.6.9
* Tensorflow 1.15.0
* Keras 2.2.4 

The goal of this repository is to detect blood cell using [BCCD Dataset](https://github.com/Shenggan/BCCD_Dataset). Automated methods to detect and classify blood cell subtypes have important applications in diagnoising blood-based diseases. The dataset annotation is in VOC data format. 
To perform blood cell detection, download the datasets and change the image file path and annotation file path in "Image Detection". To perform video detection, change the video file path in "Video Detection".

* Detect BCCD images using pretrained model ``` Yolov3_Detection.ipynb ```
* Retrain the Yolo V3 model using pretrained darknet53 convolution layers([darknet53.conv.74](https://pjreddie.com/media/files/darknet53.conv.74)) ```Yolov3_Training.ipynb```

## Outputs 
![Ground Truth](https://github.com/zil317/Yolo3//Yolo3/Results/ground_truth.png)

![Detected Image](https://github.com/zil317/Yolo3/Yolo3/Results/blood_cell_detected.png)

## Limitations
The current training process is image by image. Lots of noises found around the edges of the image. Noise reduction algorithm could be applied around the edge to improve detection accuracy.

## Acknowledgement 
https://github.com/qqwweee/keras-yolo3












