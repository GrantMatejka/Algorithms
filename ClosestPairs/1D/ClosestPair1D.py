
# O(n lg(n))
def oneDimClosestPair(arr):
   if (len(arr) > 1):
      arr.sort()
      closestPair = [0, (arr[0] - arr[1])**2]  # [idx, val]
      for i in range(len(arr)-1):
         if ((arr[i] - arr[i+1])**2 < closestPair[1]):
            closestPair = [i, (arr[i] - arr[i+1])**2]
      return closestPair

if __name__ == "__main__":
   arr = [1, 3, 6, 8, 9]
   print(oneDimClosestPair(arr))
   
   arr = [1, 2, 6, 8, 10]
   print(oneDimClosestPair(arr))
