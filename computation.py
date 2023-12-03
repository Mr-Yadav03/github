# Computing the ara of triangle using Heron's Formula
# Area = Sqrt(S*(S-a)*(S-b)*(S-c))
a = float(input("Enter the 1st side: "))
b = float(input("Enter the 2nd side: "))
c = float(input("Enter the 3rd side: "))
s = (a+b+c)/2
print("s = ",s)
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("area = ",area)