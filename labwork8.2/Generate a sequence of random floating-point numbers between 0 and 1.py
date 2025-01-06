import random
import matplotlib.pyplot as plt
float_number = random.random()
rounded_number = round(float_number,2)
plt.plot(["Random Number"], [rounded_number], color='blue')
plt.ylabel("Value")
plt.title("Random Number Visualization")
plt.show()