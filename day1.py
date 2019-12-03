
import math

def main():
    with open("my_input") as f:
        weight = f.readlines()

    # input is strings, convert to integers
    weight_i = map(int, weight)


    # perform the (floor(x/3)-2) operation
    fuel = map(lambda w: math.floor(w/3) -2, weight_i)

    total_fuel = sum(fuel)

    print(int(total_fuel))

if __name__ == "__main__":
    main()
