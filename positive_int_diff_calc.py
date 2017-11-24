print("This is warmup 1")
import sys
while True:
    x = int(input("Enter int. 1: "))
    y = int(input("Enter int. 2: "))

    if x<0 or y<0 :
        print("integers not positive")
        sys.exit(1)

    else:

         if x > y :
            a = x - y
            print(a)
         elif y > x :
              b = y - x
              print(b)
         else:
             if x == y :
                 c = 0
                 print(c)

                 sys.exit(1)







