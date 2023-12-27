import cv2

src = cv2.imread("D:/python/CV4/img/image.jpg", cv2.IMREAD_GRAYSCALE)

print(src.ndim, src.shape, src.dtype)
