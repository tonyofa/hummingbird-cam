import picamera
import time
import subprocess
import shutil


while 1:
    # capture an image and save it
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        time.sleep(2)  # Camera warm-up time
        image_path = 'capture.jpg'
        camera.capture(image_path)

    # define the path to the darknet executable
    darknet_path = '../darknet'

    # define the path to the config file, weights, and the class names
    config_path = '../yolov3-tiny.cfg'
    weights_path = '../yolov3-tiny.weights'
    class_names_path = 'darknet/cfg/coco.names'

    # run diarknet with YOLO on the image
    command = f"{darknet_path} detector test cfg/coco.data {config_path} {weights_path} {image_path} -dont-show"
    output = subprocess.check_output(command, shell=True)

    # check the output for 'bird'
    if 'bird' in output.decode():
        print('Bird detected!')
        # save the image
        shutil.copyfile(capture.jpg, f"birds/bird_{date:%Y%m%d_%H%M%S}.jpg")
    else:
        print('No bird detected.')
