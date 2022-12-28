import shutil
import facebook
import time
import cv2
import os

vid = cv2.VideoCapture("./Video/mili.mp4")
currentFrame = 0
length = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))

token = 'EAAHyLBJeZB38BABChSe5h9CssX17gMk2uUXo0tIvLiNwe8YkiI77tELxfPZA4Nr1rZAlWAGp4EtRqtZB9stJgFPU5iNfTN8Lcp3D1tFUX5l6j1GU4786F6eJq8qMPGQK0ZA8nLfBTL3dkDX1gUIpxwjcpR16FnQZCCAeZCMydlGKZAdHBvCjIUnd'
fb = facebook.GraphAPI(access_token=token)

if os.path.isdir('./frames'):
    shutil.rmtree('./frames')
    os.mkdir('./frames')

if not os.path.isdir('./frames'):
    os.mkdir('./frames')

while currentFrame < length:

    success, frame = vid.read()
    imagePath = './frames/' + str(currentFrame) + '.jpg'
    cv2.imwrite(imagePath, frame)
    image = open(imagePath, 'rb')
    fb.put_photo(image=image, message="Season 3484 out of 3956" + str(currentFrame))
    time.sleep(1)

    if os.path.isfile('./frames/' + str(currentFrame-1) + '.jpg'):
        os.remove('./frames/' + str(currentFrame-1) + '.jpg')

    currentFrame += 1
    if currentFrame == 10:
        break
