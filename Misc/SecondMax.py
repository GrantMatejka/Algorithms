def secondMaximum(arr):
   m = max(arr[0], arr[1])
   m2 = min(arr[0], arr[1])

   for i in range(2, len(arr)):
      if arr[i] > m:
         m2 = m
         m = arr[i]
      elif arr[i] > m2:
         m2 = arr[i]

   return m2


if __name__ == "__main__":

   arr = [1, 4, 3, 2, 7, 42, 678, 234, 5657, 32]
   print(secondMaximum(arr))

   arr = [-1, -4, -3, -2, -7, -42, -678]
   print(secondMaximum(arr))

   arr = [-1, -4, 3, -2, -7, -42, -678]
   print(secondMaximum(arr))

   arr = [-1, 4, 3, -2, -7, -42, -678]
   print(secondMaximum(arr))
