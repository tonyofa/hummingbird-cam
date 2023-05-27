# hummingbird-cam
ML-driven camera for photographing a hummingbird feeder with a raspberry pi 4 (32 bit).  Using generic yoloV4 model which necessitates image processing and serving via a separate server until a dedicated recognition model can be deployed on the raspberry pi as a standalone unit. yolov4-tiny can run on the pi but did not test well with recognition.  yolov4-csp is very good.  Uses standard pi 32 bit Raspian.  https://birds.tonyor.com<br>

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

### get model weights (for pre-trained generic model)
wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-csp.weights
