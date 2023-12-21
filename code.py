pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt
#stage1
TIME_STEPS = 10
DELTA_T = 1
COEFFICIENTS = [0.1, -0.5, 10]
def update_temperature_quadratic(time, coefficients):
    a, b, c = coefficients
    return a * time**2 + b * time + c
temperatures_hard_coded = [update_temperature_quadratic(t * DELTA_T, COEFFICIENTS) for t in range(TIME_STEPS)]

time_points = np.arange(0, TIME_STEPS * DELTA_T, DELTA_T)
plt.plot(time_points, temperatures_hard_coded, label='Temperature (Hard-coded)')
plt.title('Temperature Evolution Over Time (Quadratic Solution)')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature')
plt.legend()
plt.show()

#Stage2
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
user_coefficients = [a, b, c]
temperatures_keyboard_input = [update_temperature_quadratic(t * DELTA_T, user_coefficients) for t in range(TIME_STEPS)]
plt.plot(time_points, temperatures_keyboard_input, label='Temperature (Keyboard Input)')
plt.title('Temperature Evolution Over Time (Quadratic Solution)')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature')
plt.legend()
plt.show()
with open('coefficients.txt', 'r') as file:
    file_coefficients = [float(coeff) for coeff in file.readline().split(',')]
temperatures_file_input = [update_temperature_quadratic(t * DELTA_T, file_coefficients) for t in range(TIME_STEPS)]
plt.plot(time_points, temperatures_file_input, label='Temperature (File Input)')
plt.title('Temperature Evolution Over Time (Quadratic Solution)')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature')
plt.legend()
plt.show()
