import numpy as np

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(a + b)      # [11 22 33]
print(a * b)      # [10 40 90]
print(a ** 2)     # [ 1  4  9]
print(np.sqrt(b)) # [3.16 4.47 5.47]



a = np.array([10, 20, 30, 40, 50])

print(a[0])      # 10
print(a[-1])     # 50
print(a[1:4])    # [20 30 40]
print(a[a > 25]) # [30 40 50]  ← filter! very powerful