side1=int(input("enter the side1 of triangle :"))
side2=int(input("enter the side2 triangle :"))
side3=int(input("enter the side3 triangle :"))

if((side1+side2>side3) and (side2+side3>side1) and (side3+side1>side2)):
    print("YES...it is a valid triangale")
else:
    print("NO....it is not a valid triangle")

