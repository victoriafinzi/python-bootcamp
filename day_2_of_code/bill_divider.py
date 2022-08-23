
"""
If the bill was $150.00, split between 5 people, with 12% tip.
Each person should pay (150.00 / 5) * 1.12 = 33.6
Format the result to 2 decimal places = 33.60
Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.
"""
print("Welcome to the tip calculator!")
total_bill = input("What is the total bill?")
percentage_tip = input("What is the percentage tip?")
split_total_bill = input("How many people to split the bill?")
percentage_tip_calculate = (float(percentage_tip)/100) * float(total_bill)
total_payment = (float(total_bill)/int(split_total_bill)) + percentage_tip_calculate
final_amount = "{:.2f}".format(total_payment)
print(f"O total da conta para cada um será: R${final_amount}")