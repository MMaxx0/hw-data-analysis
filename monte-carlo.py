import numpy as np
import math
np.random.seed(1)

def lcg(n):
    seed = 1
    multiplier = 1103515245
    increment = 12345
    modulus = 2**31
    numbers = []
    for _ in range(n):
        seed = (multiplier * seed + increment) % modulus
        numbers.append(seed / modulus)
    return numbers

def monte_carlo_integral(func, a, b, n, custom=False):
    if custom:
        u = lcg(n)
        x = [a + (b-a) * ui for ui in u]
    else:
        x = np.random.uniform(a, b, n)
    
    y = [func(xi) for xi in x]
    return (b - a) * np.mean(y)

def f1(x):
    return np.sin(np.pi * x)

def f2(x):
    return (1/np.sqrt(2*np.pi)) * np.exp(-x**2/2)

theoretical1 = 2/np.pi 
theoretical2 = math.erf(math.sqrt(2)) / 2

n = 50000

# Python NumPy
mc1_std = monte_carlo_integral(f1, 0, 1, n, False)
mc2_std = monte_carlo_integral(f2, 0, 2, n, False)
error1_std = abs(mc1_std - theoretical1)
error2_std = abs(mc2_std - theoretical2)

# LCG 
mc1_lcg = monte_carlo_integral(f1, 0, 1, n, True)
mc2_lcg = monte_carlo_integral(f2, 0, 2, n, True)
error1_lcg = abs(mc1_lcg - theoretical1)
error2_lcg = abs(mc2_lcg - theoretical2)

print("Métodos de Monte Carlo")
print("="*60)

print(f"\n1. sin(πx) dx")
print(f"   Valor teórico: {theoretical1:.6f}")

print(f"\n2. (1/√(2π))e^(-x²/2) dx") 
print(f"   Valor teórico: {theoretical2:.6f}\n")

print(f"{'Método':<15} {'Integral 1':<12} {'Error 1':<10} {'Integral 2':<12} {'Error 2':<10}")
print("-"*60)

print(f"{'Python NumPy':<15} {mc1_std:<12.6f} {error1_std:<10.6f} {mc2_std:<12.6f} {error2_std:<10.6f}")
print(f"{'LCG':<15} {mc1_lcg:<12.6f} {error1_lcg:<10.6f} {mc2_lcg:<12.6f} {error2_lcg:<10.6f}")
print(f"{'Teórico':<15} {theoretical1:<12.6f} {'0.000000':<10} {theoretical2:<12.6f} {'0.000000':<10}")