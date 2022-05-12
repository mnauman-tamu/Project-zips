def main() :
    file_input = open("addition.data", "r")
    file_output = open("addition", "w")

    translator = {
                "add" : "00",
                "sub" : "01",
                "mul" : "02",
                "div" : "03",
                "mrmov" : "40", # "load"
                "rmmov" : "50", # "Store"
                "rrmov" : "60",
                "irmov" : "70",
                "jmp" : "90",
                "jle" : "91",
                "jl" : "92",
                "je" : "93",
                "jne" : "94",
                "jg" : "95",
                "jge" : "96",
                "halt" : "A0",
                "push" : "B1",
                "pop" : "C0",
                "call" : "D0",
                "ret" : "E0"
            }

    registers = { # all register addresses
                "%eax" : "0",
                "%ebx" : "1",
                "%ecx" : "2",
                "%edx" : "3",
                "%rsp" : "4",
                "%rbp" : "5",
            }
    file_output.write("v2.0 raw\n")
    for line in file_input :
        if line == "\n":
            continue

        line_arr = line.split()

        if '#' in line_arr[0]:
            continue

        if line_arr[0] == "halt" or line_arr[0] == "ret":
            file_output.write((translator[line_arr[0]]) + '0000\n')
            continue

        #file_output.write(hex(int(translator[line_arr[0]], 16))[2:].zfill(2))

        #file_output.write((translator[line_arr[0]]))

        if line_arr[0] == "jmp" or line_arr[0] == "je" or line_arr[0] == "jle" or line_arr[0] == "jl" or line_arr[0] == "jn" or line_arr[0] == "jne" or line_arr[0] == "jg" or line_arr[0] == "jge" or line_arr[0] == "call":
            file_output.write((translator[line_arr[0]]))
            file_output.write('FF' + line_arr[1])


        if line_arr[0] == "add" or line_arr[0] == "sub" or line_arr[0] == "mul" or line_arr[0] == "div" or line_arr[0] == "rrmov" or line_arr[0] == "mrmov" or line_arr[0] == "rmmov":
            file_output.write(translator[line_arr[0]])
            file_output.write(registers[line_arr[1]])
            file_output.write(registers[line_arr[2]] + '00')

        if line_arr[0] == "irmov":
            file_output.write(translator[line_arr[0]])
            if int(line_arr[1]) < 16:
                file_output.write(registers[line_arr[2]] + '00' + "{0:x}".format((int(line_arr[1]))))
            else:
                file_output.write(registers[line_arr[2]] + '0' + "{0:x}".format((int(line_arr[1]))))

        if line_arr[0] == "push" or line_arr[0] == "pop":
            file_output.write(translator[line_arr[0]])
            file_output.write(registers[line_arr[1]] + '001')


        """if len(line_arr) >= 2 :
            if "#" in line_arr[1]:
                continue

            if "$" in line_arr[1] : # for immediate values, I write as hex
                file_output.write(hex(int(line_arr[1][1:]))[2:].zfill(2))

            elif "(" in line_arr[1]:
                file_output.write(hex(int(registers[line_arr[1][1:-1]]))[2:].zfill(2))

            else :
                file_output.write(hex(int(registers[line_arr[1]]))[2:].zfill(2))
        else :
            file_output.write("00")

        if len(line_arr) >= 3 :
            if "#" in line_arr[2]:
                continue

            if "$" in line_arr[2] : # for immediate values, write as hex
                file_output.write(hex(int(line_arr[2][1:]))[2:].zfill(2))

            elif "(" in line_arr[2]:
                if line_arr[2][0] == "(" :
                    file_output.write(hex(int(registers[line_arr[2][1:-1]]))[2:].zfill(2))

            else :
                file_output.write(hex(int(registers[line_arr[2]]))[2:].zfill(2))

        else :
            file_output.write("00")"""
        file_output.write("\n")

    file_input.close()
    file_output.close()

if __name__ == "__main__":
    main()