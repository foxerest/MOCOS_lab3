import numpy as math
import time

amountSum, amountMultiplication = 0, 0


def random_signal():
    return math.random.uniform(-1, 1)


def fast_fourier_transform(f):
    global amountSum, amountMultiplication
    n = len(f)
    if n == 1:
        return f
    else:
        even, odd = fast_fourier_transform(f[::2]), fast_fourier_transform(f[1::2])
        factor = math.exp(-2j * math.pi * math.arange(n) / n)
        amountSum += 2
        amountMultiplication += 3
        return math.concatenate([even + factor[:n // 2] * odd, even + factor[n // 2:] * odd])


def print_message():
    print(" k                      c_k                    ")
    for i in range(amount_input):
        print(" {:<3}   {:<39.15f} ".format(i, C_ks[i]))
    print("\nЗагальний час обчислення коефіцієнтів:", time)
    print("Загальна кількість операцій додавання:", amountSum)
    print("Загальна кількість операцій множення:", amountMultiplication)


n = 8
amount_input = 2 ** n
func = [random_signal() for _ in range(amount_input)]
start = time.time()
C_ks = fast_fourier_transform(func)
time = time.time() - start
print_message()
