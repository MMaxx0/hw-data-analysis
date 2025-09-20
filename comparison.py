import matplotlib.pyplot as plt
import random


def lcg(seed, multiplier, increment, modulus, count):
    numbers = []
    current = seed
    for _ in range(count):
        numbers.append(current)
        current = (multiplier * current + increment) % modulus
    return [x / modulus for x in numbers]


def histograms():
    n = 10000
    lcg_data = lcg(1, 1103515245, 12345, 2**31, n)

    random.seed(1)
    python_data = [random.random() for _ in range(n)]

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.hist(lcg_data, bins=30, alpha=0.7, color="blue", edgecolor="black")
    plt.title("LCG")
    plt.xlabel("Generated Number")
    plt.ylabel("Frequency")
    plt.grid(True, alpha=0.3)

    plt.subplot(1, 2, 2)
    plt.hist(python_data, bins=30, alpha=0.7, color="orange", edgecolor="black")
    plt.title("Python random()")
    plt.xlabel("Generated Number")
    plt.ylabel("Frequency")
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("histograms/lcg_vs_python.png")


histograms()
