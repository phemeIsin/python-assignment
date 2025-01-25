#a program to check if a number is divisible by 11
number=int(input("Enter a number: "))
if(number%11 == 0):  #check if it is or not divisible by 11
    print(number,"is divisible by 11")
else:
    print(number,"is not a multiple of 11")
