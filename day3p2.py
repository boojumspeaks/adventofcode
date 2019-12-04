
def main():
    with open("input_day_3") as f:
        lines = f.readlines()

    codes = list(map(code_parser, lines))

    locations = list(map(location_calculator, codes))

    intersections = []
    c = 0
    for i in locations[0]:

        c += 1
        if c % 1000 == 0:
            print(c)

        if i in locations[1]:
            intersections.append(i)

    distance = find_td_min(filter(
        lambda x: x != (0, 0), intersections), codes[0], codes[1])

    print("result")
    print(distance)


def find_td_min(intersections, codes1, codes2):
    distances_1 = location_calculator_distance(codes1)
    distances_2 = location_calculator_distance(codes2)

    intersection_distances = []
    for i in intersections:
        d1 = list(filter(
            lambda x: i[0] == x[0] and i[1] == x[1], distances_1))[0]
        d2 = list(filter(
            lambda x: i[0] == x[0] and i[1] == x[1], distances_2))[0]

        intersection_distances.append(d1[2]+d2[2])

    min_val = min(intersection_distances)
    return min_val


def location_calculator_distance(codes):
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


def location_calculator(codes):
    x = 0
    y = 0
    locations = []

    for (c, d) in codes:
        if c == 'U':
            locations = locations + [(x, y + o) for o in range(d)]
            y = y + d
        elif c == 'D':
            locations = locations + [(x, y - o) for o in range(d)]
            y = y - d
        elif c == 'R':
            locations = locations + [(x + o, y) for o in range(d)]
            x = x + d
        elif c == 'L':
            locations = locations + [(x - o, y) for o in range(d)]
            x = x - d
        else:
            raise Exception("invalid direction code")

    return locations


def code_parser(codes):
    list_codes = codes.split(",")
    split_codes = list(map(lambda x: (x[0], int(x[1:])), list_codes))

    return split_codes


def test_data1():
    # test data
    # distance 610
    val1_1 = code_parser("R75,D30,R83,U83,L12,D49,R71,U7,L72")
    val1_2 = code_parser("U62,R66,U55,R34,D71,R55,D58,R83")

    locs_11 = location_calculator(val1_1)
    locs_12 = location_calculator(val1_2)

    intersections = filter(lambda x: x in locs_12, locs_11)

    distance = find_td_min(filter(
        lambda x: x != (0, 0), intersections), val1_1, val1_2)
    print(distance)


def test_data2():
    # distance 410
    val2_1 = code_parser("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51")
    val2_2 = code_parser("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")

    locs_21 = location_calculator(val2_1)
    locs_22 = location_calculator(val2_2)

    intersections = filter(lambda x: x in locs_22, locs_21)

    distance = find_td_min(filter(
        lambda x: x != (0, 0), intersections), val2_1, val2_2)
    print(distance)


if __name__ == "__main__":
    test_data1()
    test_data2()
    main()
