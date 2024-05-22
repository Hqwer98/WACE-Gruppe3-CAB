from typing import Callable


class TrapezoidalRule:
    n = 1
    weight = [0.5, 0.5]
    A = 0

    def calculate_integral(self, f: Callable[[float], float], a: float, b: float):
        h = (b - a) / self.n
        for i in range(0, self.n + 1):
            xi = a + i * h
            self.A += self.weight[i] * f(xi)
            print(i)
            print(xi)
            print(f(xi))
            print(self.weight[i] * f(xi))
            print(self.A)
            print("-----------")
        return self.A
