import shutil
import facebook
import time
import cv2
import os
import You2Dow

link = input("Enter the YouTube video URL: ")

while link != "q":

    if os.path.isdir('./Video'):
        shutil.rmtree('./Video')
        os.mkdir('./Video')

    You2Dow.Download(link)
    yt = You2Dow.YouTube(link)
    title = yt.title

    vid = cv2.VideoCapture("./Video/"+title+".mp4")
    currentFrame = 1
    length = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))

    token = 'EAAHyLBJeZB38BANjm3mb5cxllT3ZA0XZBcUzsZA2cHtut0tkGI8qsZAKcZCZBYZBwZByxqSx7gslZBJzdc6DVVVIxWV9DEQjRNXOfNZCNKP7y1TAcLJOdWyVoPCBvNY8imXn26Q6qmZAlkJGXnZB7Tnd2V6LoINBcgN2DK5ZAwhdi68ZAJIe9Qn6mlrZBZCmjJYWjCpMxtUYPZCTYe8BZAkfwZDZD'
    fb = facebook.GraphAPI(access_token=token)


    if not os.path.isdir('./frames'):
        os.mkdir('./frames')

    while currentFrame <= length:

        success, frame = vid.read()
        imagePath = './frames/' + str(currentFrame) + '.jpg'
        cv2.imwrite(imagePath, frame)
        image = open(imagePath, 'rb')
        fb.put_photo(image=image, message="dd")
        print("Uploaded "+str(currentFrame))
        time.sleep(1)

        if os.path.isfile('./frames/' + str(currentFrame-1) + '.jpg'):
            os.remove('./frames/' + str(currentFrame-1) + '.jpg')

        currentFrame =+ 1

    currentFrame = 1
    link = input("Enter the YouTube video URL: ")