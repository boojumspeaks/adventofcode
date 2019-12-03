
import math

def fuel_weight(w):
    fuel_f = 0

    if w/3 - 2 > 0:
        fuel_w = math.floor(w/3) - 2
        fuel_f = fuel_weight(fuel_w) + fuel_w

    return fuel_f

def main():
    with open("my_input") as f:
        weight = f.readlines()

    # input is strings, convert to integers
    weight_i = map(int, weight)


    # perform the (floor(x/3)-2) operation
    fuel = map(fuel_weight, weight_i)

    total_fuel = sum(fuel)

    print(int(total_fuel))

if __name__ == "__main__":
    main()
