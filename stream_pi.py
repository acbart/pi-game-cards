# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
from pyzbar.pyzbar import decode
import time
import cv2
import json
from say_something import say
from play_music import Jukebox
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
# allow the camera to warmup
time.sleep(0.1)

jukebox = Jukebox()

say("Give me a music card, so I can play it.")

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    # show the frame
    cv2.imshow("Frame", image)
    # Do work!
    #data,bbox,rectifiedImage = qrDecoder.detectAndDecode(image)
    #if len(data)>0:
    #    print("Decoded Data : {}".format(data))
    qrs_found = decode(image)
    try:
        results = [json.loads(qr.data) for qr in qrs_found]
        if results:
            #comments = "and".join(str(r['id']) for r in results)
            #say(comments)
            first_song_id = results[0]['id']
            say(jukebox.get_song(first_song_id).name)
            jukebox.switch_to(first_song_id)
    except KeyError as f:
        say("I don't know song {}".format(f))
    except Exception as e:
        print(e)
        
    
    # Process keyboard
    key = cv2.waitKey(1) & 0xFF
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break