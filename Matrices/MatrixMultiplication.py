# assuming n x n matrices
def dumbMultiply(A, B):
   dim = len(A)
   C = [[0 for i in range(dim)] for j in range(dim)]

   for i in range(dim):
      for j in range(dim):
         C[i][j] = 0
         for k in range(dim):
            C[i][j] = C[i][j] + (A[i][k] * B[k][j])
   return C

# TODO
# dimension of matrix has to be power of 2
def recursiveMatrixMult(A, B):
   if (len(A) == 1):
      return [[A[1][1] * B[1][1]]]
   else:
      # 4 submatrices of A: A1 A2 A3 A4
      # 4 submatrices of B: B1 B2 B3 B4
      # Recursively calculate 8 matrix products
      # return result
      print("Not incorporated")

# TODO
# given two n x n matrices produces matrix of their product
def strassenMultiply():
   if (len(A) == 1):
      return [[A[1][1] * B[1][1]]]
   else:
      # 4 submatrices of A: A1 A2 A3 A4
      # 4 submatrices of B: B1 B2 B3 B4
      # Recursively calculate 7 matrix products (secret sauce step)
      # return result (cleverly choose additions and subtractions computed previously)
      print("Not incorporated")

if __name__ == '__main__':
   # only working with n x n matrices
   A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
   B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

   print(dumbMultiply(A, B))
