n = int(input())
a_list = [int(elem) for elem in input().split()]

count = 0

while True:
    if count not in a_list:
        print(count)
        break
    count += 1
