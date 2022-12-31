import shutil
import facebook
import time
import cv2
import os
import You2Dow

link = "https://www.youtube.com/watch?v=M9dVG82QynM&ab_channel=IRAJ"
You2Dow.Download(link)
yt = You2Dow.YouTube(link)
title = yt.title

vid = cv2.VideoCapture("./Video/" + title + ".mp4")
currentFrame = 1
fake = 1
length = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))

token = 'EAAHyLBJeZB38BAB7jLM96FKYB0bm4q3vHCqxIiS2itOgKG1VHZCdxpvoyPMp4OeqipiTh4r4Gd86LGb8p4GnE62DADkuK11xRMqZB1GoBtZBZBmnlhC9kedyfUTk17k16GhVRkMC6DjxpJ2SVvZBcol4L60HuK8Phvq8ZCa3x4KCGMUAKzzl8OD'
fb = facebook.GraphAPI(access_token=token)

if not os.path.isdir('./frames'):
    os.mkdir('./frames')

while currentFrame < length:

    success, frame = vid.read()
    imagePath = './frames/' + str(currentFrame) + '.jpg'
    cv2.imwrite(imagePath, frame)
    image = open(imagePath, 'rb')
    fb.put_photo(image=image, message=title + " " + str(fake) + " out of " + str(length//2))
    fake += 1
    print("Uploaded " + str(currentFrame))
    time.sleep(0.5)

    if os.path.isfile('./frames/' + str(currentFrame - 2) + '.jpg'):
        os.remove('./frames/' + str(currentFrame - 2) + '.jpg')

    currentFrame += 2

time.sleep(86400)
