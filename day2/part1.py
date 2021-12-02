with open("input.txt", "r") as file:
	commands = file.readlines()

# Sample Inputs:
# with open("sample.txt", "r") as file:
# 	commands = file.readlines()

horizontal = 0
depth = 0

for command in commands:
  commandAsArray = command.rstrip().split(' ')
  direction = commandAsArray[0]
  num = int(commandAsArray[1])

  if direction == "forward":
    horizontal += num
  elif direction == "up":
    depth -= num
  else: # "down"
    depth += num

print(horizontal * depth)

