f = open("input.txt", 'r')

nums = f.readlines()
numArray = [int(i) for i in nums]

# sample input
# numArray = [199,200,208,210,200,207,240,269,260,263]

count = 0

def compareSumThree(array, i):
  return array[i+1] + array[i+2] + array[i+3] > array[i] + array[i+1] + array[i+2]

for i in range (len(numArray) - 3):
  if compareSumThree(numArray,i):
    count = count + 1

print(count)