def main():
    n = int(input())
    a_list = [int(elem) for elem in input().split()]
    b_list = [int(elem) for elem in input().split()]

    ans_1 = ans_2 = 0

    for a, b in zip(a_list, b_list):
        if a == b:
            ans_1 += 1
        elif a in b_list:
            ans_2 += 1

    print(ans_1)
    print(ans_2)

if __name__ == "__main__":
    main()
