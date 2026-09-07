import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5, 5, 100)
y = x**2
plt.plot(x, y)
plt.show()

x = np.linspace(-5, 5, 100)
y1=np. sin(x)
y2=np. cos(x)
plt.plot (x,y1, label="sin(x)")
plt. plot (x,y2, label="cos(x)")
plt.legend()
plt. show ()

#The reason for adding a () after the function is to call the function
x=np. linspace(-3,3,500)
y=np.exp(-x**2)
plt. plot (x,y)
plt. show()

