#simple program to calculate volume of a sphere (with the formula 3/4*pi*r**3)
import math  #adds the math lib 
radius=int(input("Enter the radius ")) #radius input
pi=math.pi
rc=(radius**3)
volume=(4/3*pi*rc)
print(f"Volume of the sphere is {volume:.2f}") #answer in 2dp
