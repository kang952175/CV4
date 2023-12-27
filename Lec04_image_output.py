import cv2

src = cv2.imread("D:/python/CV4/img/image.jpg", cv2.IMREAD_GRAYSCALE)

cv2.namedWindow("src", flags=cv2.WINDOW_KEEPRATIO)
cv2.resizeWindow("src", 600, 400)
cv2.imshow("src", src)
cv2.waitKey(0)
cv2.destroyWindow("src")
