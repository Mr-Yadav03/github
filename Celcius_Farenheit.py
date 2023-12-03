# # Celsius to Fahrenheit conversion
# c = float(input("Enter Celsius value to convert into Fahrenheit: "))
# f = (c*(9/5)+32)
# print("°F ",f) 

# # Circumference and area of circle
# # area = pi*r^2,Circumference = 2*pi*r
# pi = 3.14
# r =  float(input("Enter the radius of circle: "))
# area = pi*r**2
# cirucumference = 2*pi*r
# print("area of circle: ",area)
# print("circumference of circle: ",cirucumference)

# Area of Triangle = (1/2)*b*h
# Area = Sqrt(S*(S-a)*(S-b)*(S-c))
a = float(input("Enter the 1st side: "))
b = float(input("Enter the 2nd side: "))
c = float(input("Enter the 3rd side: "))
s = (a+b+c)/2
print("s = ",s)
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("area = ",area)