def fibonacciRecursive(num):
   if num <= 1:
      return num
   else:
      return (fibonacciRecursive(num-1) + fibonacciRecursive(num-2))

def fibonacciDynamic(num):
   fibArr = []

   for i in range(num + 1):
      if i == 0:
         fibArr.append(0)
      elif i <= 2:
         fibArr.append(1)
      else:
         fibArr.append(fibArr[i-1] + fibArr[i-2])

   return fibArr[num]

if __name__ == "__main__":

   for i in range(10):
      print("{} : {} | {}".format(i, fibonacciRecursive(i), fibonacciDynamic(i)))
