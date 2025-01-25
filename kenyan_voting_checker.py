#a simple program to check if one is eligible to vote.they are if above 18 and kenyan citizens else,not eligle 
age=int(input("Please Enter your age.\nAge:")) #age input
if (age>=18):  #checking age
    citizenship =input("enter your citizenship.\nCitizenship:").lower() #citizenship input
    if (citizenship == "kenyan"):#citizenship checking
        print("You are eligible to vote")
    else:
        print("You are  not eligible to vote.\n(one must be a kenyan citizen.)")
else :
    print("you are under age hence not eligible to vote")

    
