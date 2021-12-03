# Use sample inputs
# with open("sample.txt", "r") as file:
#     raw_binaries = file.readlines()

with open("input.txt", "r") as file:
    raw_binaries = file.readlines()

# Handle raw_binaries
binaries = map(lambda x: x.rstrip(), raw_binaries)
binaries_rows = len(binaries)
binaries_columns = len(binaries[0])


# Init oxygen and co2 value with binaries
oxygen = list(binaries)
co2 = list(binaries)


# Get oxygen generator rating, return as an array
def get_oxygen(array, columns):
    for position in range(columns):
        zero_count = 0
        temp = []
        for binary in array:
            if int(binary[position]) == 0:
                zero_count += 1
                temp.append(binary)

        if zero_count > len(array) / 2:
            array = list(temp)
        else:
            array = [bina for bina in array if bina not in temp]

        if len(array) == 1:
            break;
    return array


# Get CO2 scrubber rating, return as an array
def get_co2(array, columns):
    for position in range(columns):
        zero_count = 0
        temp = []
        for binary in array:
            if int(binary[position]) == 0:
                zero_count += 1
                temp.append(binary)

        if zero_count > len(array) / 2:
            array = [bina for bina in array if bina not in temp]
        else:
            array = list(temp)

        if len(array) == 1:
            break;
    return array


# Transform them into binary
oxygen_binary = int(get_oxygen(oxygen, binaries_columns)[0])
co2_binary = int(get_co2(co2, binaries_columns)[0])


# Calculate decimal from a binary
def binary_to_decimal(binary):
    bit_position = 0
    decimal = 0
    while binary > 0:
        current_bit = binary % 10
        decimal += current_bit * pow(2, bit_position)
        binary = binary // 10
        bit_position += 1
    return decimal


# Transform them into decimal
oxygen_decimal = binary_to_decimal(oxygen_binary)
co2_decimal = binary_to_decimal(co2_binary)


# Final result
print("What is the life support rating of the submarine?")
print(oxygen_decimal * co2_decimal)
