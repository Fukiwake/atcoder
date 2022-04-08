def main():
    v, a, b, c = [int(elem) for elem in input().split()]

    while True:
        v -= a
        if v < 0:
            print("F")
            break

        v -= b
        if v < 0:
            print("M")
            break

        v -= c
        if v < 0:
            print("T")
            break


if __name__ == "__main__":
    main()
