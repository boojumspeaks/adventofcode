

def main():
    with open("input_day_2") as f:
        opcodes = f.readline()

    # set up commands
    ops = opcodes.split(",")

    intcode = map(int, ops)

    program_counter = 0

    # modifications due to fire
    intcode[1] = 12
    intcode[2] = 2

    # main operation loop, add, multiply or halt
    while(intcode[program_counter] != 99):

        # Addition
        if intcode[program_counter] == 1:

            # set up registers
            register_1 = intcode[program_counter + 1]
            register_2 = intcode[program_counter + 2]
            location = intcode[program_counter + 3]

            value_1 = intcode[register_1]
            value_2 = intcode[register_2]
            intcode[location] = value_1 + value_2

            program_counter = program_counter + 4

        # multiplication
        elif intcode[program_counter] == 2:

            # set up registers
            register_1 = intcode[program_counter + 1]
            register_2 = intcode[program_counter + 2]
            location = intcode[program_counter + 3]

            value_1 = intcode[register_1]
            value_2 = intcode[register_2]
            intcode[location] = value_1 * value_2

            program_counter = program_counter + 4

        # exit
        elif intcode[program_counter] == 99:
            break

        else:
            raise Exception("invalid opcode")

    return intcode


if __name__ == "__main__":
    result = main()
    print(result[0])
