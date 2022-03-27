
print("Welcome to the tip calculate")

total_bill = float(input("What was your total bill amount"))
tip_perc = int(input("how much tip are you gonna give 10, 15 or 20"))
people = int(input("How many people are you goimg to split the bill between?"))

tip_as_perc = tip_perc / 100
total_tip_amt = total_bill * tip_as_perc
total_bill_amt = total_bill + total_bill
amt_per_person = round(total_bill / people) 
print(f"each person should pay {amt_per_person}")




