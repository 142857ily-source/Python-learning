import numpy as np
import matplotlib.pyplot as plt

x=0
y=0
x_position=[0]
y_position=[0]
for i in range(int(input((f"Enter your steps:")))):
    direction=np. random. randint(0,4)
    if direction == 0:
        x+=1
    elif direction == 1:
        x-=1
    elif direction == 2:
        y+=1
    elif direction ==3:
        y-=1
    x_position .append (x)
    y_position .append (y)
    distance=((((x_position[-1])**2)+((y_position[-1])**2))**0.5)
print (distance)
plt.plot(x_position, y_position)
plt.scatter(0, 0, s=100)
plt.axis("equal")
plt.show()



