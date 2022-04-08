# x1, y1 = [int(elem) for elem in input().split()]
# x2, y2 = [int(elem) for elem in input().split()]
# x3, y3 = [int(elem) for elem in input().split()]

# if (x1 == x2 or x1 == x3) and (y1 == y2 or y1 == y3):
#     if x1 == x2:
#         x4 = x3
#     elif x1 == x3:
#         x4 = x2

#     if y1 == y2:
#         y4 = y3
#     elif y1 == y3:
#         y4 = y2
# elif (x2 == x1 or x2 == x3) and (y2 == y1 or y2 == y3):
#     if x1 == x2:
#         x4 = x3
#     elif x1 == x3:
#         x4 = x2

#     if y1 == y2:
#         y4 = y3
#     elif y1 == y3:
#         y4 = y2

import collections

x_list = []
y_list = []


for _ in range(3):
    x, y = [int(elem) for elem in input().split()]

    x_list.append(x)
    y_list.append(y)

x_count = collections.Counter(x_list)
y_count = collections.Counter(y_list)

for k, v in x_count.items():
    if v == 1:
        result_x = k

for k, v in y_count.items():
    if v == 1:
        result_y = k

print(result_x, result_y)
