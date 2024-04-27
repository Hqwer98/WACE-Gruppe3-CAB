import numpy as np

test = 123
print(test)

print("Hello World!")
print("moin moin meister nase")

print("Test-C")


def apply(x):
    return x / 1


def f(x):
    return np.square(x) + 1


x_point = 2

delta_x = 1

f_ableitung = (f(x_point + delta_x) - f(x_point) / delta_x)

print("Ableitung von f(x) an der Stelle x=", x_point, "ist", f_ableitung)
