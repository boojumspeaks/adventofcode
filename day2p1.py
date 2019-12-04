

def main():
    with open("input_day_2") as f:
        opcodes = f.readline()

    # set up commands
    ops = opcodes.split(",")

    intcode = map(int, ops)

    # modifications due to fire
    intcode[1] = 12
    intcode[2] = 2

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


if __name__ == "__main__":
    result = main()
    print(result[0])
