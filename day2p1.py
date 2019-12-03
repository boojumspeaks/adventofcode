

def main():
    with open("input_day_2") as f:
        opcodes = f.readline()


    ops = opcodes.split(",")

    intcode = map(int, ops)

    operation_count = 0

    # modifications due to fire
    intcode[1] = 12
    intcode[2] = 2

    # main operation loop, add, multiply or halt
    while(intcode[operation_count] != 99):

        if intcode[operation_count] == 1:
            value_1 = intcode[intcode[operation_count+1]]
            value_2 = intcode[intcode[operation_count+2]]
            location = intcode[operation_count+3]
            intcode[location] = value_1 + value_2

            operation_count = operation_count + 4

        elif intcode[operation_count] == 2:
            value_1 = intcode[intcode[operation_count+1]]
            value_2 = intcode[intcode[operation_count+2]]
            location = intcode[operation_count+3]
            intcode[location] = value_1 * value_2

            operation_count = operation_count + 4

        else:
            raise Exception("invalid opcode")

    return intcode
    



if __name__ == "__main__":
    result = main()
    print(result[0])
