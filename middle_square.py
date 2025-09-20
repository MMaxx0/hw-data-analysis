import matplotlib.pyplot as plt
import numpy as np


def middle_square(seed, digits=4):
    numbers = []
    current = seed
    width = digits * 2
    for _ in range(10000):
        numbers.append(current)
        squared = str(current**2).zfill(width)
        mid = len(squared) // 2
        current = int(squared[mid - digits // 2 : mid + digits // 2])
        if current == 0:
            break
    max_value = 10**digits - 1
    normalized_numbers = [x / max_value for x in numbers]

    plt.hist(normalized_numbers, bins=30, edgecolor="black", linewidth=1.2)
    plt.title("Middle Square Histogram")
    plt.xlabel("Generated Number")
    plt.ylabel("Frequency")
    plt.grid(True, alpha=0.3)
    plt.savefig("histograms/middle_square_hist.png")
    plt.close()

    print("=== Pruebas de Hipótesis ===")

    bins = 30
    n = len(normalized_numbers)
    e = n / bins
    counts, _ = np.histogram(normalized_numbers, bins=bins, range=(0.0, 1.0))
    coef = np.sum((counts - e) ** 2 / e)
    chisq_95 = 17.70

    print(f"Prueba de Uniformidad:")
    print(f"  Coef = {coef:.2f}")
    print(f"  Chi^2_95 = {chisq_95}")

    def autocorr(x, k):
        x = np.asarray(x)
        n = len(x)
        xbar = x.mean()
        num = np.dot(x[: n - k] - xbar, x[k:] - xbar)
        den = np.dot(x - xbar, x - xbar)
        return num / den

    print(f"\nPrueba de Independencia:")
    x = np.array(normalized_numbers).reshape(-1)

    for k in (1, 2, 3, 4, 5):
        if len(x) - k <= 0:
            break
        r = autocorr(x, k)
        z = r * np.sqrt(len(x))
        print(k, r, "z≈", z)


middle_square(seed=9238, digits=4)
