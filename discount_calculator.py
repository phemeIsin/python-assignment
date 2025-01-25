#a discount calculator that adds a 10% discount to goods above 5000 and 5% to goods above 1000
print("Hello there!")
while True:
    try:
        amount = float(input("Please enter the total cost of the goods ")) #amnt input
        if amount>5000:
            d1 = amount-(amount*0.1)#amount calculation after discount
            print("Discount applied.\nAmount payable is ", d1)
            break
        elif 1000 < amount <= 5000:
            d2 = amount-(amount * 0.05)#amount calculation after discount
            print("Discount applied.\nAmount payable is ", d2)
            break
        else:#if goods not worth 1000+
            print("No discount applied.\nAmount payable is ", amount)
            break
    except ValueError: #if user enters letters instead of numbers
        print("Please enter the amount in numbers only!(eg:2000).")
