# hummingbird-cam
ML-driven camera for photographing a hummingbird feeder with a raspberry pi 4 (32 bit).  Using generic model yolov4 which necessitates image processing to server until a dedicated recognition model can be deployed on the raspberry pi as a standalone unit. yolov4-tiny does not do well with recognition but yolov4-csp is very good.<br>
#
clone to pi, set up ssh keys from pi to pc, copy server to PC and configure<br>
## preparation from base OS image
### required packages (apt - cam and server) 
sudo apt install python3-opencv libopencv-dev
### required packages (pip - cam only)
pip install picamera
### darknet install & config (server only)
git clone https://github.com/AlexeyAB/darknet<br>
cd darknet<br>
sed -i 's/OPENCV=0/OPENCV=1/' Makefile<br>
### enable CUDA support for darknet (not required)
sed -i 's/CUDNN=0/CUDNN=1/' Makefile<br>
sed -i 's/CUDNN_HALF=0/CUDNN_HALF=1/' Makefile<br>
otherwise CUDNN=0, CUDNN+HALF = 0<br>
make<br>
### tiny-YOLO 
wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-csp.weights
