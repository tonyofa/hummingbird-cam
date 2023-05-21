# hummingbird-cam
ML-driven camera for photographing a hummingbird feeder with a raspberry pi 4
### required packages (apt)
python3-pip, python3-opencv, libopencv-dev
### required packages (pip)
picamera, numpy
### darknet install & config
git clone https://github.com/AlexeyAB/darknet<br>
cd darknet<br>
sed -i 's/OPENCV=0/OPENCV=1/' Makefile<br>
sed -i 's/CUDNN=0/CUDNN=1/' Makefile<br>
sed -i 's/CUDNN_HALF=0/CUDNN_HALF=1/' Makefile<br>
make<br>
### tiny-YOLO install
wget https://pjreddie.com/media/files/yolov3-tiny.weights
