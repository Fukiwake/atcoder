from threading import current_thread


def main():
    n = int(input())
    t = input()

    x = y = 0
    current_direction = "east"

    for t_word in t:
        if t_word == "S":
            if current_direction == "east":
                x += 1
            elif current_direction == "west":
                x += -1
            elif current_direction == "north":
                y += 1
            elif current_direction == "south":
                y += -1
        if t_word == "R":
            if current_direction == "east":
                current_direction = "south"
            elif current_direction == "west":
                current_direction = "north"
            elif current_direction == "north":
                current_direction = "east"
            elif current_direction == "south":
                current_direction = "west"

    print(x, y)



if __name__ == "__main__":
    main()
