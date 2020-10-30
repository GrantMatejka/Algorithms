# Easiest way to reverse a string in python but doesn't show much algorithmic skill
def builtInReverse(str):
   return str[::-1]


def reverse(arr):
   for i in range(len(arr) // 2):
      temp = arr[i]
      arr[i] = arr[len(arr) - 1 - i]
      arr[len(arr) - 1 - i] = temp
   return arr

if __name__ == "__main__":
   arr = [0, 1, 2, 3, 4]
   print(arr)
   print(builtInReverse(arr))
   print(reverse(arr))

   arr = [0, 1, 2, 3, 4 ,5]
   print(arr)
   print(builtInReverse(arr))
   print(reverse(arr))
