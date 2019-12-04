
def main():
    with open("input_day_3") as f:
        lines = f.readlines()

    codes = map(code_parser, lines)

    locations = list(map(location_calculator, codes))

    intersections = []
    c = 0
    for l in locations[0]:
        c += 1
        if c % 1000 == 0:
            print(c)
        l_intersect = list(filter(lambda x: x[0] == l[0] and x[1] == l[1], locations[1]))
        intersections = intersections + l_intersect

    distance = []
    for l in intersections:
        corr_int = list(filter(lambda x: x[0] == l[0] and x[1] == l[1], locations[0]))[0]
        distance.append(corr_int)


    print(distance)
    print(intersections)


def location_calculator(codes):
    x = 0
    y = 0
    td = 0
    locations = []

    for (c, d) in codes:
        if c == 'U':
            locations = locations + [(x, y + o, td + o) for o in range(d)]
            y = y + d
            td = td + d
        elif c == 'D':
            locations = locations + [(x, y - o, td + o) for o in range(d)]
            y = y - d
            td = td + d
        elif c == 'R':
            locations = locations + [(x + o, y, td + o) for o in range(d)]
            x = x + d
            td = td + d
        elif c == 'L':
            locations = locations + [(x - o, y, td + o) for o in range(d)]
            x = x - d
            td = td + d
        else:
            raise Exception("invalid direction code")

    return locations


def code_parser(codes):
    list_codes = codes.split(",")
    split_codes = list(map(lambda x: (x[0], int(x[1:])), list_codes))

    return split_codes


def test_data1():
    # test data
    # distance 159
    val1_1 = code_parser("R75,D30,R83,U83,L12,D49,R71,U7,L72")
    val1_2 = code_parser("U62,R66,U55,R34,D71,R55,D58,R83")


    locs_11 = location_calculator(val1_1)
    locs_12 = location_calculator(val1_2)

    intersections = []
    for l in locs_11:
        l_intersect = list(filter(lambda x: x[0] == l[0] and x[1] == l[1], locs_12))
        intersections = intersections + l_intersect

    for l in intersections:
        corr_int = list(filter(lambda x: x[0] == l[0] and x[1] == l[1], locs_11))[0]
        print(corr_int)
        print(l)
        print(corr_int[2] + l[2])

def test_data2():
    # distance 135
    val2_1 = code_parser("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51")
    val2_2 = code_parser("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")


    locs_21 = location_calculator(val2_1)
    locs_22 = location_calculator(val2_2)

    intersections = []
    for l in locs_21:
        l_intersect = list(filter(lambda x: x[0] == l[0] and x[1] == l[1], locs_22))
        intersections = intersections + l_intersect

    for l in intersections:
        corr_int = list(filter(lambda x: x[0] == l[0] and x[1] == l[1], locs_21))[0]
        print(corr_int)
        print(l)
        print(corr_int[2] + l[2])




if __name__ == "__main__":
    main()
