# A peak is any element greater than both of its neighbors

def linearPeakFind(arr):
   # check edge cases and single element arr
   if (len(arr) == 1):
      return 0
   elif (arr[0] >= arr[1]):
      return 0
   elif (arr[len(arr)-1] >= arr[len(arr)-2]):
      return len(arr)-1

   for i in range(len(arr)-1):
      # if element greater than both neighbors return index
      if (arr[i] >= arr[i-1] and arr[i] >= arr[i+1]):
         return i

def divideConquerPeakFinder(arr):
   


if __name__ == "__main__":
   arr = [1, 2, 3, 4, 5, 4, 3, 2, 6, 7, 5, 4]
   print("index of peak: {}".format(linearPeakFind(arr)))
