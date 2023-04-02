import shutil
import facebook
import time
import cv2
import os
import You2Dow

link = "Enter your youtube link here"
# https://www.youtube.com/watch?v=jNQXAC9IVRw&ab_channel=jawed

You2Dow.Download(link)
yt = You2Dow.YouTube(link)
title = yt.title

vid = cv2.VideoCapture("./Video/" + title + ".mp4")
currentFrame = 1
limit = 4
startFrame = 5000

length = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))

token = 'Your facebook API token'
fb = facebook.GraphAPI(access_token=token)

if not os.path.isdir('./frames'):
    os.mkdir('./frames')

while currentFrame < length:

    success, frame = vid.read()
    imagePath = './frames/' + str(currentFrame) + '.jpg'

    if (currentFrame % limit) == 0 and currentFrame > startFrame:
        cv2.imwrite(imagePath, frame)
        image = open(imagePath, 'rb')
        fb.put_photo(image=image, message=title + " " + str(currentFrame//limit) + " out of " + str(length//limit))
        print("Uploaded " + str(currentFrame))
        time.sleep(60)

    if os.path.isfile('./frames/' + str(currentFrame - 1) + '.jpg'):
        os.remove('./frames/' + str(currentFrame - 1) + '.jpg')

    currentFrame += 1

time.sleep(86400)

