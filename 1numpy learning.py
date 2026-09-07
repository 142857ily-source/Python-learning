import numpy as np
x = np.array ([1, 2, 3, 4, 5])
print(x)
print(x* 2)
print(x**2)

# np.arange(start, stop, step), stop does not included
# difference between range() and np. arange() 
# is that we can enter noninteger as the step in np. arange()
x = np.arange(0, 2, 0.2)
print(x)

# no. linspace(x,y,z) means take z points evenly from the interval [x,y]
# stop does included
x = np.linspace(0, 10, 6)
print(x)


x = np.linspace(-5, 5, 100)
y = x**2
for value in y:
    print(f"{value:.2f}")