f = open("input.txt", 'r')

nums = f.readlines()
numArray = [int(i) for i in nums]

# sample input
# numArray = [199,200,208,210,200,207,240,269,260,263]

count = 0

# First Attempt:
# ----------------
# def compareSumThree(array, i):
#   return array[i+1] + array[i+2] + array[i+3] > array[i] + array[i+1] + array[i+2]

# for i in range (len(numArray) - 3):
#   if compareSumThree(numArray,i):
#     count = count + 1


# A better solution:
# ------------------
# for i in range (len(numArray) - 3):
#   if numArray[i+3] > numArray[i]:
#     count = count + 1


# Or this can be the best:
def compareSumThree(array, i):
  return array[i+3] > array[i]

for i in range (len(numArray) - 3):
  if compareSumThree(numArray,i):
    count = count + 1

print(count)

f.close()  # It's important to close the file when I'm done with it.