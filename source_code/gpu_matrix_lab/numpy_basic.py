import numpy as np

a = np.array([1, 2, 3, 4, 5])   # from a list
b = np.zeros(5)                   # [0. 0. 0. 0. 0.]
c = np.ones(5)                    # [1. 1. 1. 1. 1.]
d = np.arange(0, 10, 2)          # [0 2 4 6 8]
e = np.random.rand(5)             # 5 random numbers 0-1

print("Array a:", a)
print("Array b:", b)
print("Array c:", c)
print("Array d:", d)
print("Array e:", e)


# ------------------------------------------------------------------------------

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a.shape)   # (2, 3) ← 2 rows, 3 columns
print(a.ndim)    # 2      ← 2-dimensional
print(a.size)    # 6      ← total elements