
def increasing(x):
    str_x = str(x)
    for i in range(len(str_x) - 1):
        if str_x[i] > str_x[i + 1]:
            return False
    
    return True


def duplicate(x):
    str_x = str(x)
    for i in range(len(str_x) - 1):
        if str_x[i] == str_x[i + 1]:
            return True

    return False



def main():
    puzzle_input = range(245318, 765749)

    dups = filter(duplicate, puzzle_input)
    inc = list(filter(increasing, dups))

    print((inc))
    print(len(inc))



if __name__ == "__main__":
    main()
