f = open("input.txt", 'r')

nums = f.readlines()
numArray = [int(i) for i in nums]

# sample input
# numArray = [199,200,208,210,200,207,240,269,260,263]

count = 0

for i in range (len(numArray) - 1):
  if numArray[i+1] >  numArray[i]:
    count = count + 1

print(count)

f.close()  # It's important to close the file when I'm done with it.