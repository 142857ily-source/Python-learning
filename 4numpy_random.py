import numpy as np
# np. random. random generates a number between 0 and 1 randomly
x = np.random. random()
y = np. random. random(5)
z = np. random. random ((2,3))
print(x) 
print (y)
print (z)

# last input is the size
coins = np.random.randint(0, 2, 10) 
print(coins)

coins = np.random.randint(0, 2, size=1000000)
print (np. mean (coins))

# for NumPy, true = 1 and false = 0
dice = np.random.randint(1, 7, size=100000)
print (np. mean (dice==6))
