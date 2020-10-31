def power(a, b):
   if b == 1:
      return a
   else:
      a2 = a * a
      recurA = power(a2, b//2)
   
   if b % 2 == 0:
      return recurA
   else:
      return a * recurA


if __name__ == '__main__':
   print(power(2, 8))