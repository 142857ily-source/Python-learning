# P = initial money
P = float(input("Enter your principal:"))
while P < 0:
     print("Error! Principal cannot be negative.")
     P = float(input("Enter your principal again:"))
else:
# r = annual rate
     r = 0.04
# t= number of years
     t = float(input("Enter the number of years you wish to deposit the money:"))
     if t>0 and t<=50:
# F = final result
         F=P*((1+r)**t)
         print(f"Your final amount will be ${F:,.2f}.")
     else: 
         print("The time has to be between 0 and 50 years.")
         t = float(input("Enter the number of years you wish to deposit the money:"))
         F=P*((1+r)**t)
         print(f"Your final amount will be ${F:,.2f}.")




