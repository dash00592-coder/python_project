print("Welcome to the tip calculator! ")
total_bill = float(input("what was the total bill ? $"))
tip_percent = float(input("what percentage of bill are you willing to pay tip ?"))
share = int(input("how many people would you like to share the bill ? "))
final_bill = total_bill +(total_bill * (tip_percent / 100) ) 
per_head_bill = final_bill / share
print(f"each person has to pay ${per_head_bill}")
