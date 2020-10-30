# O(n^2)
def slowCountInversions(arr):
   countOfInversions = 0
   for i in range(len(arr)):
      for j in range(i, len(arr)):
         if (arr[i] > arr[j]):
            countOfInversions += 1
   
   return countOfInversions;

# O(nlg(n))
# returns [count of inversions, sorted array]
# Builds off of merge sort so pretty cool bc it's fast and sorts and counts inversions
def betterCountInversions(arr):
   countOfInversions = 0

   if (len(arr) <= 1):
      return 0, arr
   else:
      # Counting left/right side inversions
      # then need to count inversions over middle
      leftInversions, leftSorted = betterCountInversions(arr[0:len(arr)//2])
      rightInversions, rightSorted = betterCountInversions(arr[len(arr)//2:len(arr)])
      splitInversions, sortedList = countAndSortSplitInversions(leftSorted, rightSorted)
      countOfInversions = leftInversions + rightInversions + splitInversions

      return countOfInversions, sortedList

def countAndSortSplitInversions(arrA, arrB):
   i = 0
   j = 0
   splitInversions = 0
   retArr = []
   while i < len(arrA) and j < len(arrB):
      if arrA[i] <= arrB[j]:
         retArr.append(arrA[i])
         i += 1
      else:
         retArr.append(arrB[j])
         j += 1
         # however many items are left in A are 'inversions over' the element from B
         splitInversions += (len(arrA) - i)

   while (i != len(arrA)):
       retArr.append(arrA[i])
       i += 1

   while (j != len(arrB)):
       retArr.append(arrB[j])
       j += 1

   return splitInversions, retArr


if __name__ == "__main__":
   invArr = [1, 3, 5, 2, 4, 6, 6]
   print(slowCountInversions(invArr))
   print(betterCountInversions(invArr))
