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


age = float(input("Enter your age: "))
while age < 0:
    print("Age cannot be negative.")
    age = float(input("Enter your age again: "))
print("Accepted.")

# input always gives a string.
# : → indicates the start of the formatting specification
# , → adds a thousands separator
# .2f → formats the number as a floating-point number with two decimal places




