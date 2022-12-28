import shutil
import facebook
import time
import cv2
import os

vid = cv2.VideoCapture("./Video/mili.mp4")
currentFrame = 0
length = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))

token = 'EAAHyLBJeZB38BAPpU85omUM1tg1uAUju09notQ1UEBQ02mclJWymd7rxZCA4IPnbgoVpRz8D0A3oCCeWXvAbURHheV3hZBhxSqQTjmbxssGYZAOyudPo0HVx5ZBZC1fWUEhfZCfZBfB0xXDbNe5rJjO1f7KkJroLhSzXbzRcKbnuutrqGbBfzpQeNlGU1ke9ZAfzlfpSnhBjFXQZDZD'
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
