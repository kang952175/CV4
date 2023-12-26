import numpy as np

array = np.array([[1, 2, 3],
                  [4, 5, 6]])

print(f"ex01: \n{array.ndim}")
print(f"ex01: \n{array.shape}")
print(f"ex01: \n{array.dtype}")

array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([1, 2, 3], dtype=complex, ndmin=3)
array3 = np.array(array1, copy=False)
array4 = np.array(np.mat('1 2; 3 4'), subok=True)

array1[0] = [4, 5, 6]

print(f"ex02: \n{array1}")
print(f"ex02: \n{array2}")
print(f"ex02: \n{array3}")
print(f"ex02: \n{type(array4)}")

array1 = np.array([1, 2, 3])
array2 = np.array([[1, 2],
                   [3, 4]])
array3 = np.array([[[1, 2],
                    [3, 4]],
                   [[5, 6],
                    [7, 8]]])

print(f"ex03: \n{array1[-1]}")
print(f"ex03: \n{array2[0][1]}")
print(f"ex03: \n{array3[0][1][1]}")

array = np.array([[[1, 2],
                   [3, 4]],
                  [[5, 6],
                   [7, 8]]])

for i in array[0]:
    for j in i:
        if j % 2 == 0:
            print(f"ex04: \n{j}")

array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20]])

print(f"ex04: \n {array[1:3]}")
print(f"ex04: \n {array[::2]}")
print(f"ex04: \n {array[2:,1::2]}")

array = np.arange(12)

reshape1 = array.reshape(2, 3, 2)
reshape2 = np.reshape(array, (2, -1), order='F')

print(f"ex05: \n {reshape1}")
print(f"ex05: \n {reshape2}")

array = np.arange(4)

axis1 = array[np.newaxis]
axis2 = array[:, np.newaxis]

print(f"ex06: \n {axis1}")
print(f"ex06: \n {axis2}")

array = np.arange(12).reshape(3, -1)

flat1 = array.flatten(order='F')
flat2 = array.ravel()

print(f"ex07: \n {flat1}")
print(f"ex07: \n {flat2}")

array1 = np.arange(6).reshape(2, 3)
array2 = np.arange(6, 12).reshape(2, 3)

merge1 = np.stack([array1, array2], axis=0)
merge2 = np.stack([array1, array2], axis=-1)

print(f"ex08: \n {merge1}")
print(f"ex08: \n {merge2}")

array = np.arange(10).reshape(2, 5)

detach1 = np.split(array, 2, axis=0)
detach2 = np.split(array, [2, 3], axis=1)

print(f"ex09(raw data): \n {array}")
print(f"ex09: \n {detach1}")
print(f"ex09: \n {detach2}")

array1 = np.array([1, 2, 3, 4]).reshape(2, 2)
array2 = np.array([1.5, 2.5])

add = array1 + array2

print(f"ex10: \n {add}")

array1 = np.array([1, 2, 3, 4]).reshape(2, 2)
array2 = np.array([5, 6, 7, 8]).reshape(2, 2)

mat1 = np.mat(array1)
mat2 = np.mat(array2)

print(f"ex11: \n {mat1.T * mat2}")
print(f"ex11: \n {mat1 ** 2}")

array = np.zeros((1280, 1920, 3), np.uint8)

x, y, w, h = 100, 100, 300, 300
roi = array[x:x+w, y:y+h]

print(f"ex12: \n {array.shape}")
print(f"ex12: \n {roi.shape}")

array = np.zeros((1280, 1920, 3), np.uint8)

coi = array[:, :, 0]

print(f"ex13: \n {array.shape}")
print(f"ex13: \n {coi.shape}")
