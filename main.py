import shutil
import facebook
import time
import cv2
import os

vid = cv2.VideoCapture("./Video/mili.mp4")
currentFrame = 0
length = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))

token = 'EAAHyLBJeZB38BAJiSUK7foFdFAQ2K0tKFjkkxJupTb7xdfmR6sZAGTAfBcXv1QG7GnEROVWRFXRB4kzHJ8lnSLW6xP8qkONXYAgXKZAnWGXYJPWp6ZCR0ZB938k4Ub9JHAkAeOMkNEatzJqQrXyEg2M9VtqyeZAwOD0ZCpXiNzMqyCshYvFsrrZA'
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
