def MergeSort(arr):
   if (len(arr) <= 1):
      return arr

   # this is where the divide and conquer happens
   left = MergeSort(arr[:len(arr)//2])
   right = MergeSort(arr[(len(arr)//2):])

   # now put the lists back together
   return Merge(left, right)

def Merge(arrA, arrB):
   idxA = 0
   idxB = 0
   retArr = []

   # Loop while in the range of both arrays to combine into a sorted array
   while idxA < len(arrA) and idxB < len(arrB):
      if (arrA[idxA] < arrB[idxB]):
         retArr.append(arrA[idxA])
         idxA += 1
      else:
         retArr.append(arrB[idxB])
         idxB += 1

   # Make sure all elements from array A are represented
   while idxA < len(arrA):
      retArr.append(arrA[idxA])
      idxA += 1

   # Now check elements of array B
   while idxB < len(arrB):
      retArr.append(arrB[idxB])
      idxB += 1

   return retArr

if __name__ == "__main__":
   unsorted = [1000, 1 ,3 ,76 ,42 ,12]
   print(unsorted)
   sortedArr = MergeSort(unsorted)
   print(sortedArr)
