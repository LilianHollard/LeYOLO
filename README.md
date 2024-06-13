![alt text](gitimg/LeYOLO-logo.png)


# Abstract
-> Read paper : (arXiv link)

Computational efficiency in deep neural networks is critical for object detection, especially as newer models prioritize speed over efficient computation (FLOP). This evolution has somewhat left behind embedded and mobile-oriented AI object detection applications. In this paper, we focus on design choices of neural network architectures for efficient object detection computation based on FLOP and propose several optimizations to enhance the efficiency of YOLO-based models.

Firstly, we introduce an efficient backbone scaling inspired by inverted bottlenecks and theoretical insights from the Information Bottleneck principle. Secondly, we present the Fast Pyramidal Architecture Network (FPAN), designed to facilitate fast multiscale feature sharing while reducing computational resources. Lastly, we propose a Decoupled Network-in-Network (DNiN) detection head engineered to deliver rapid yet lightweight computations for classification and regression tasks.

Building upon these optimizations and leveraging more efficient backbones, this paper contributes to a new scaling paradigm for object detection and YOLO-centric models called LeYOLO. Our contribution consistently outperforms existing models in various resource constraints, achieving unprecedented accuracy and flop ratio. Notably, LeYOLO-Small achieves a competitive mAP score of 38.2% on the COCO val with just 4.5 FLOP(G), representing a 42% reduction in computational load compared to the latest state-of-the-art YOLOv9-Tiny model while achieving similar accuracy. Our novel model family achieves a FLOP-to-accuracy ratio previously unattained, offering scalability that spans from ultra-low neural network configurations (< 1 GFLOP) to efficient yet demanding object detection setups (> 4 GFLOPs) with 25.2, 31.3, 35.2, 38.2, 39.3 and 41 mAP for 0.66, 1.47, 2.53, 4.51, 5.8 and 8.4 FLOP(G).

![alt text](gitimg/final.png)


# LeYOLO Results

LeYOLO familly model results on MSCOCO val dataset.
You can find pre-trained weight on the weights folder.

| Models           | mAP | Image Size     | FLOP (G) |
|------------------|-----|----------------|----------|
|LeYOLONano        |25.2 | 320            | 0.66     |
|LeYOLOSmall       |31.3 | 320            | 1.47     |
|LeYOLONano        |35.2 | 640            | 2.53     |
|LeYOLOSmall       |28.2 | 640            | 4.51     |
|LeYOLOMedium      |39.3 | 640            | 5.80     |
|LeYOLOLarge       |41.0 | 768            | 8.40     |

## Reproductability

Reproduct LeYOLO results by using cfg file.
We did not use any expansive or fancy training methods, just classic and default Ultralytics training receipes.
We enable non-computer scientist to perform fast training reproductability for their own research with very easy training methods!


# LeYOLO installation and quickstart

## Install
- Warning ! Upgrading pip might be necessary 
	```
	python3 -m pip install --upgrade pip
	```
- Go into root folder
	```
	pip install -e .
	```

## Quickstart
Use CLI or python interface to use LeYOLO / YOLOv8

- Minimal example can be found in minimal.ipynb notebook.