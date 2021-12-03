# Use sample inputs
# with open("sample.txt", "r") as file:
# 	raw_binaries = file.readlines()

with open("input.txt", "r") as file:
	raw_binaries = file.readlines()

# Handle raw_binaries
binaries = map(lambda x: list(x.rstrip()), raw_binaries)
binaries_rows = len(binaries)
binaries_columns = len(binaries[0])


# Find the gamma rate, return as an array of bits(int)
def get_gamma_rate(array, columns, rows):
	gamma_rate = []
	for c in range(columns):
		zero_count = 0
		for r in range(rows):
			if int(array[r][c]) == 0:
				zero_count += 1
		if zero_count > rows / 2:
			gamma_rate.append(0)
		else:
			gamma_rate.append(1)
	return gamma_rate


gamma_binary_array = get_gamma_rate(binaries, binaries_columns, binaries_rows)


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


# Calculate gamma rate (decimal)
string_gamma_binary = [str(b) for b in gamma_binary_array]
gamma_binary = int(''.join(string_gamma_binary))
gamma_decimal = binary_to_decimal(gamma_binary)


# Calculate epsilon rate (decimal) from gamma rate (decimal)
def get_epsilon_from_gamma(g_binary, g_decimal):
	bits = len(str(g_binary))
	epsilon = pow(2, bits) - 1 - g_decimal
	return epsilon


epsilon_decimal = get_epsilon_from_gamma(gamma_binary, gamma_decimal)


# Final result
print("What is the power consumption of the submarine?")
print(gamma_decimal * epsilon_decimal)
