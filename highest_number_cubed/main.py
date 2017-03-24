"""This is the entry point of the program."""


def highest_number_cubed(limit):
    Num = 0
    CubeNum = 0
    while CubeNum < limit:
        Num += 1
        CubeNum = Num**3
    return Num-1