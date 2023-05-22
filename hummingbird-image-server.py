import cv2
import numpy as np
import os
import subprocess
import shutil
from datetime import datetime

# hummingbird-cam image processing...
# pick up image from pi and look for birds using darknet / yolov.  Ideally this would all run on the pi,
# but the yolov-tiny models don't see the birds as well as the yolov-4
# next module should be used to train on birds vs no-birds to build a dedicated hummingbird model then
# todo:  port the image processing with a dedicated model so it can run standalone on the raspberry pi 

# Parameters
host = 'tony@hummingbird' # raspberry pi 4
source_path = '/home/tony/hummingbird-cam/capture.jpg'
local_path = './image.jpg'
bird_dir = './birds'
#nobird_dir = './nobirds' # may be useful for training standalone model for the pi someday.
model_cfg = '/darknet/cfg/yolov4-csp.cfg'
model_weights = './yolov4-csp.weights'



while True:
    # Copy file from Raspberry Pi
    subprocess.call(['scp', f'{host}:{source_path}', local_path])

    # Load image
    img = cv2.imread(local_path)
    
    # define the path to the darknet executable
    darknet_path = './darknet/darknet'

    # # define the path to the config file, weights, and the class names
    config_path = './darknet/cfg/yolov4-csp.cfg'
    weights_path = './yolov4-csp.weights'
    class_names_path = './darknet/cfg/coco.names'
    cfg_path = './darknet/cfg'

    # run diarknet with YOLO on the image
    command = f"{darknet_path} detector test {cfg_path}/coco.data {config_path} {model_weights} -dont_show {local_path}"
    output = subprocess.check_output(command, shell=True)

    suffix = datetime.now().strftime('%Y%m%d%H%M%S')
 
    # check the output for 'bird'
    if 'bird' in output.decode():
        print(f'Bird detected! {suffix}')
        # save the image
        shutil.move(local_path, os.path.join(bird_dir, f'img_{suffix}.jpg'))
     else:
        print(f'No bird detected. {suffix}')
    cv2.destroyAllWindows()