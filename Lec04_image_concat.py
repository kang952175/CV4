import cv2
import numpy as np

# (H, W, C)

one = cv2.imread("./img/one.jpg")
two = cv2.imread("./img/two.jpg")
three = cv2.imread("./img/three.jpg")
four = cv2.imread("./img/four.jpg")

one = cv2.resize(one, (390, 366))
two = cv2.resize(two, (256, 244))
three = cv2.resize(three, (390, 281))
four = cv2.resize(four, (256, 403))

horizontal1 = np.full((50, one.shape[1], 3), [0, 0, 0], dtype=np.uint8)
horizontal2 = np.full((50, two.shape[1], 3), (0, 0, 0), dtype=np.uint8)

left = cv2.vconcat((one, horizontal1, three))
# left = np.vstack((one, horizontal1, three))
# right = cv2.vconcat((two, horizontal2, four))
right = np.vstack((two, horizontal2, four))

vertical = np.full((left.shape[0], 50, 3), 0, dtype=np.uint8)

dst = cv2.hconcat((left, vertical, right))
# dst = np.hstack((left, vertical, right))
# dst = np.concatenate((left, line, right), axis = 1)

cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()
