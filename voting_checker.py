#simple program that asks user for age and citizenship and checks if they are eligible based on age and citizenship(should be above 18 years and either a kenyan,ugandan or tanzanian citizen 
age = int(input("Please enter your age: ")) #age input
if age >= 18: #checking age
    citizenship = int(input("Choose your citizenship:\n1. Kenyan\n2. Ugandan\n3. Tanzanian\n4. Other\nChoice: "))
    if citizenship == 1 or citizenship == 2 or citizenship == 3: #checking citizenship
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.\n(You must be a citizen of either of the three countries).")
else:
    print("You are not eligible to vote.")
