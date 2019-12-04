
def increasing(x):
    str_x = str(x)

    for i in range(len(str_x) - 1):
        if str_x[i] > str_x[i + 1]:
            return False
    
    return True


def duplicate_by_2(x):
    str_x = str(x)

    if str_x[0] == str_x[1] and str_x[1] != str_x[2]:
        return True
    if str_x[1] == str_x[2] and str_x[2] != str_x[3] and str_x[1] != str_x[0]:
        return True
    if str_x[2] == str_x[3] and str_x[3] != str_x[4] and str_x[2] != str_x[1]:
        return True
    if str_x[3] == str_x[4] and str_x[4] != str_x[5] and str_x[3] != str_x[2]:
        return True
    if str_x[4] == str_x[5] and str_x[4] != str_x[3]:
        return True

    return False





def main():
    puzzle_input = range(245318, 765749)

    dups = filter(duplicate_by_2, puzzle_input)
    inc = list(filter(increasing, dups))

    print((inc))
    print(len(inc))



if __name__ == "__main__":
    main()
