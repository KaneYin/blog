import numpy as np
import matplotlib.pyplot as plt

# define the activation function
def uFun(num):
    if num >= 0:
        return 1
    else:
        return 0
    
# define the neural network
def nn(x, y):
    num1 = uFun(x - y + 1)
    num2 = uFun(-x - y + 1)
    num3 = uFun(-x)
    result = uFun(num1 + num2 - num3 - 1.5)
    return result

# generate 1000 points with in [-2, 2]
N = 1000
points = np.random.uniform(-2, 2, (N, 2))

colors = []
for (x, y) in points:
    output = nn(x, y)
    if output == 0:
        colors.append("blue")
    else:
        colors.append("red")

# plot
plt.figure(figsize=(6,6))
plt.scatter(points[:,0], points[:,1], c=colors, s=10)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Neural Network Classification in [-2,2]^2")
plt.grid(True)
plt.show()