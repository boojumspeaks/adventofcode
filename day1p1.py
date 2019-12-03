
import math

def main_for_loop():
    with open("my_input") as f:
        weight = f.readlines()

    value = 0
    for w in weight:
        value = value + math.floor(int(w)/3) - 2

    return int(value)

def main():
    with open("my_input") as f:
        weight = f.readlines()

    # input is strings, convert to integers
    weight_i = map(int, weight)


    # perform the (floor(x/3)-2) operation
    fuel = map(lambda w: math.floor(w/3) - 2, weight_i)

    total_fuel = sum(fuel)

    ret_val = (int(total_fuel))
    return ret_val

def main_few_lines():
    with open("my_input") as f:
        return int(sum(map(lambda w: math.floor(int(w)/3) - 2, f.readlines())))

if __name__ == "__main__":
    print("main normal")
    print(main())
    print("main for")
    print(main_for_loop())
    print("main compressed")
    print(main_few_lines())
