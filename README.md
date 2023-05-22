# hummingbird-cam
ML-driven camera for photographing a hummingbird feeder with a raspberry pi 4 (64 bit Raspian)
## preparation from base OS image
### required packages (apt - cam and server) 
sudo apt install python3-opencv libopencv-dev
### required packages (pip - cam only)
pip install picamera
### darknet install & config (server only)
git clone https://github.com/AlexeyAB/darknet<br>
cd darknet<br>
sed -i 's/OPENCV=0/OPENCV=1/' Makefile<br>
### enable CUDA support for darknet
sed -i 's/CUDNN=0/CUDNN=1/' Makefile<br>
sed -i 's/CUDNN_HALF=0/CUDNN_HALF=1/' Makefile<br>
make<br>
### tiny-YOLO 
wget https://pjreddie.com/media/files/yolov3-tiny.weights
