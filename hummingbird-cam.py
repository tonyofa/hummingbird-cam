import picamera, time
from datetime import datetime

#this just captures images with the pi
# yolov-tiny models will run locally on the pi, but the recognition wasn't spectacular so moved the image processing from the pi to a PC (server)

# captures images, saves locally
camera =  picamera.PiCamera()
camera.resolution = (3280, 2464)
camera.rotation = 180 # if the pi image is upside down
time.sleep(2)  # Camera warm-up time
image_path = 'capture.jpg'
while True:
   
    camera.capture(image_path)

    print(f"wrote image at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    time.sleep(5) # allow some time for the server to pick it up a static file - this could be a lot better but it works for the initial testing

   