import cv2
import numpy as np

filename ="../images/cctv.mp4"
capture = cv2.VideoCapture(filename)

while True:
    _, img1 = capture.read()
    _, img2 = capture.read()

    diff = cv2.absdiff(img1, img2)
    
    diff_gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    diff_blur = cv2.GaussianBlur(diff_gray, (5,5,), 0)

    _, binary_img = cv2.threshold(diff_blur, 20, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(binary_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        x, y, b, l = cv2. boundingRect(contour)
        if cv2.contourArea(contour) > 300:
            cv2.rectangle(img1, (x, y), (x+b, y+l), (0,255,0), 2)
    
    cv2.imshow("Motion", img1)
    key = cv2.waitKey(1)
    if key%256 == 27:
        print("Closing program")
        exit()

