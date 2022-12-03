import cv2
import matplotlib.pyplot as plt

interest_img = cv2.imread("../images/4.jpg")

cropped_img = interest_img

test_images = [
    "../images/1.jpg",
    "../images/2.jpg",
    "../images/3.jpg",
    "../images/4.jpg",
    "../images/5.jpg",
    "../images/6.jpg",
    "../images/7.jpg",
    "../images/8.jpg",
    "../images/9.jpg",
    "../images/10.jpg"
]

correlations = []

for img in test_images:
    testImg = cv2.imread(img)
    croppedTestImg = testImg
    plt.imshow(croppedTestImg)
    plt.show()
    X = croppedTestImg - cropped_img
    ssd = sum(X[:]**2)
    correlations.append(ssd)

print(correlations)

# cv2.imshow("image of interest",interest_img)
# plt.imshow(cropped_img)
# plt.show()