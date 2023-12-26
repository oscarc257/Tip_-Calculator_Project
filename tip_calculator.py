#If the bill was $150.00, split between 5 people, with 12% tip.

print("Welcome to the tip calculator!")
#Input bill amount total; Data type float for more accurate results. 
bill = float(input("What was the total bill? $"))
#Input tip amount desired from choices given,
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
#Enter the number of people splitting the bill with.
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: $ {final_amount}")

# Less code with a similar result:
#bill_with_tip = bill * (1 + tip/100)
#print(f"Each person should pay: $ {bill_with_tip / people:.2f}")
