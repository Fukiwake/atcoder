import math

A, B = [int(elem) for elem in input().split()]

d = math.sqrt(A**2 + B**2)

print(A/d, B/d)

# 平方根の計算方法
# import math
# math.sqrt(x)
