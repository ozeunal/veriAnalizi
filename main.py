import random
import matplotlib.pyplot as plt

def calculate_r(x, y):
    mean_x = sum(x) / len(x)
    a = [(x_i - mean_x) ** 2 for x_i in x]
    b = sum(a) / len(a)
    sd_x = b ** 0.5

    mean_y = sum(y) / len(y)
    a = [(y_i - mean_y) ** 2 for y_i in y]
    b = sum(a) / len(a)
    sd_y = b ** 0.5

    t = 0
    for i in range(len(x)):
        x_z_or_standard_value = (x[i] - mean_x) / sd_x
        y_z_or_standard_value = (y[i] - mean_y) / sd_y
        t = t + x_z_or_standard_value * y_z_or_standard_value

    return t / len(x)

x = [random.randint(20, 60) for i in range(20)]
y = [random.randint(50, 100) for i in range(20)]
plt.scatter(x, y, marker='x')
calculate_r(x, y)
print(calculate_r(x,y))
plt.show()


