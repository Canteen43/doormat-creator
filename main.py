# python 3

def print_door_mat(length: int) -> None:
    if (length <= 1) or (length % 2 == 0):
        print("Length must be odd and greater than 1.")
        return
    middle = length // 2
    coordinates = {'x': 0, 'y': 0}
    while coordinates['y'] < length:
        while coordinates['x'] < length:
            if coordinates['y'] == middle and coordinates['x'] == middle - 1:
                print("-WELCOME-", end="")
                coordinates['x'] += 2
            elif (coordinates['y'] != middle and
                  abs(coordinates['x'] - middle) + abs(coordinates['y'] - middle) <= middle):
                print(".|.", end="")
            else:
                print("---", end="")
            coordinates['x'] += 1
        print("")
        coordinates['y'] += 1
        coordinates['x'] = 0


if __name__ == '__main__':
    n = input("Enter the size of the door mat: ")
    if n.isdigit():
        print_door_mat(int(n))
    else:
        print("We need a valid integer!")
