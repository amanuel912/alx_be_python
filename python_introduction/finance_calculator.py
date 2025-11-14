income = int(input("Enter your monthly income:"))
expense = int(input("Enter your total monthly expense"))
monthly_savings = income - expense
projected_saving = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))
print(f"Your monthly savings are {monthly_savings}")
print(f"Projected savings after one year, with interest, is: {projected_saving}")