def distance(p1, p2):
   return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def minPairOfThreePairs(p1, p2, p3):
   disP1 = distance(p1[0], p1[1])
   disP2 = distance(p2[0], p1[1])
   disP3 = distance(p3[0], p3[1])

   if disP1 < disP2 and disP1 < disP3:
      return p1
   elif disP2 < disP1 and disP2 < disP3:
      return p2
   else:
      return p3

# O(n lg(n))
# len(px) must be >= 3
def twoDimClosestPair(px, py):
   if len(px) == 2:
      return [px[0], px[1]]

   elif len(px) == 3:
      disP1 = distance(px[0], px[1])
      disP2 = distance(px[0], px[2])
      disP3 = distance(px[1], px[2])

      if disP1 < disP2 and disP1 < disP3:
         return [px[0], px[1]]
      elif disP2 < disP1 and disP2 < disP3:
         return [px[0], px[2]]
      else:
         return [px[1], px[2]]

   else:
      leftX = px[len(px)//2:]
      leftY = sorted(px[len(px)//2:], key=lambda point: point[1])
      rightX = px[:len(px)//2]
      rightY = sorted(px[:len(px)//2], key=lambda point: point[1])

      closestLeft = twoDimClosestPair(leftX, leftY)
      closestRight = twoDimClosestPair(rightX, rightY)

      closestSplit = closestSplitPair(px, py,
          min(distance(closestLeft[0], closestLeft[1]), distance(closestRight[0], closestRight[1])))

      print(closestLeft)
      print(closestRight)
      print(closestSplit)

      return minPairOfThreePairs(closestLeft, closestRight, closestSplit)


def closestSplitPair(x, y, dist):
   medianX = x[len(x)//2][0]
   potentialPoints = [p for p in y if p[0] < medianX + dist and p[0] > medianX - dist]

   bestDist = dist
   bestPair = [x[0], x[1]]

   for i in range(len(potentialPoints)-1):
      for j in range(i+1, min(7, len(potentialPoints)-i)):
         if distance(potentialPoints[i], potentialPoints[i+j]) < bestDist:
            bestDist = distance(potentialPoints[i], potentialPoints[i+j])
            bestPair = [potentialPoints[i], potentialPoints[i+j]]

   return bestPair


if __name__ == "__main__":
   arr = [[0, 1], [0, 3], [5, 3], [9, 6], [3.5,4]]
   print(twoDimClosestPair(sorted(arr, key=lambda point: point[0]), sorted(arr, key=lambda point: point[1])))
