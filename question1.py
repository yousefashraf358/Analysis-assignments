import time
import matplotlib.pyplot as plt


def power_iterative(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

def divideconquer(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        temp = divideconquer(base, exponent // 2)
        return temp * temp
    else:
        temp = divideconquer(base, (exponent - 1) // 2)
        return base * temp * temp
    

exponents = [10**i for i in range(7)]
duration_iterative = []
duration_divide_conquer = []


for exponent in exponents:
    start_time_iterative = time.time()
    power_iterative(2, exponent)
    end_time_iterative = time.time()
    duration_iterative.append((end_time_iterative - start_time_iterative) * 1000)

    start_time_divide_conquer = time.time()
    divideconquer(2, exponent)
    end_time_divide_conquer = time.time()
    duration_divide_conquer.append((end_time_divide_conquer - start_time_divide_conquer) * 1000)


plt.plot(exponents, duration_iterative, label='iterative')
plt.plot(exponents, duration_divide_conquer, label='divide and conquer')
plt.xlabel('exponent')
plt.ylabel('duration (ms)')
plt.legend()
plt.show()