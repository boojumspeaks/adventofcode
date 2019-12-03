
def intcode_interpreter(intcode):

    instruction_pointer = 0

    # main operation loop, add, multiply or halt
    while(intcode[instruction_pointer] != 99):

        # Addition
        if intcode[instruction_pointer] == 1:

            # set up registers
            register_1 = intcode[instruction_pointer + 1]
            register_2 = intcode[instruction_pointer + 2]
            location = intcode[instruction_pointer + 3]

            value_1 = intcode[register_1]
            value_2 = intcode[register_2]
            intcode[location] = value_1 + value_2

            instruction_pointer = instruction_pointer + 4

        # multiplication
        elif intcode[instruction_pointer] == 2:

            # set up registers
            register_1 = intcode[instruction_pointer + 1]
            register_2 = intcode[instruction_pointer + 2]
            location = intcode[instruction_pointer + 3]

            value_1 = intcode[register_1]
            value_2 = intcode[register_2]
            intcode[location] = value_1 * value_2

            instruction_pointer = instruction_pointer + 4

        # exit
        elif intcode[instruction_pointer] == 99:
            instruction_pointer = instruction_pointer + 1
            break

        else:
            raise Exception("invalid opcode")

    return intcode


def main():
    with open("input_day_2") as f:
        opcodes = f.readline()

    # set up commands
    ops = opcodes.split(",")

    intcode = list(map(int, ops))

    # modifications due to fire
    for i in range(99):
        for j in range(99):
            intcode_test = intcode.copy()
            intcode_test[1] = i
            intcode_test[2] = j

            result = intcode_interpreter(intcode_test)
            if result[0] == 19690720:
                print(100 * i + j)

    return result


if __name__ == "__main__":
    result = main()
    print(result[0])
