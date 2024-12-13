Monthly_Income = int(input("Enter your monthly income:"))
Monthly_Expenses = int(input("Enter your total monthly expenses: ")) 
Monthly_Savings = Monthly_Income - Monthly_Expenses 
Annual_Interest = .05
#Calculate the projected savings after one year, incorporating the interest. 
# Use the simplified formula for annual savings projection: (Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)).
Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * Annual_Interest)
print("Your monthly savings are $",Monthly_Savings)
print("Projected savings after one year, with interest, is: $",Projected_Savings)