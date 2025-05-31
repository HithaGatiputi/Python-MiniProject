print("welcome to tip calculator")
bill = float(input("What is your total bill the Rs.?  "))
people = int(input("How many people to split the bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
tip_percentage = tip / 100
total_tip_amount = bill*tip_percentage
total_bill = bill + total_tip_amount
per_person_bill = total_bill / people
print(per_person_bill)