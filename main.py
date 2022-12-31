import shutil
import facebook
import time
import cv2
import os
import You2Dow

link = "https://www.youtube.com/watch?v=M9dVG82QynM&ab_channel=IRAJ"
# https://www.youtube.com/watch?v=jNQXAC9IVRw&ab_channel=jawed

You2Dow.Download(link)
yt = You2Dow.YouTube(link)
title = yt.title

vid = cv2.VideoCapture("./Video/" + title + ".mp4")
currentFrame = 1
limit = 8
length = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))

token = 'EAAHyLBJeZB38BAB7jLM96FKYB0bm4q3vHCqxIiS2itOgKG1VHZCdxpvoyPMp4OeqipiTh4r4Gd86LGb8p4GnE62DADkuK11xRMqZB1GoBtZBZBmnlhC9kedyfUTk17k16GhVRkMC6DjxpJ2SVvZBcol4L60HuK8Phvq8ZCa3x4KCGMUAKzzl8OD'
fb = facebook.GraphAPI(access_token=token)

if not os.path.isdir('./frames'):
    os.mkdir('./frames')

while currentFrame < length:

    success, frame = vid.read()
    imagePath = './frames/' + str(currentFrame) + '.jpg'

    if (currentFrame % limit) == 0:
        cv2.imwrite(imagePath, frame)
        image = open(imagePath, 'rb')
        fb.put_photo(image=image, message=title + " " + str(currentFrame//limit) + " out of " + str(length//limit))
        print("Uploaded " + str(currentFrame))
        time.sleep(10)

    # if os.path.isfile('./frames/' + str(currentFrame - 1) + '.jpg'):
    #     os.remove('./frames/' + str(currentFrame - 1) + '.jpg')

    currentFrame += 1

time.sleep(86400)

