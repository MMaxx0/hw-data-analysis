import matplotlib.pyplot as plt
import numpy as np


def blum(prime1, prime2, seed):
    m = prime1 * prime2
    numbers = []
    for _ in range(10000):
        numbers.append(seed)
        seed = (seed**2) % m
    normalized_numbers = [x / m for x in numbers]

    plt.hist(normalized_numbers, bins=30, edgecolor="black", linewidth=1.2)
    plt.title("Blum Histogram")
    plt.xlabel("Generated Number")
    plt.ylabel("Frequency")
    plt.grid(True, alpha=0.3)
    plt.savefig("histograms/blum_hist.png")
    plt.close()

    print("=== Pruebas de Hipótesis ===")

    bins = 30
    n = len(normalized_numbers)
    e = n / bins
    counts, _ = np.histogram(normalized_numbers, bins=bins, range=(0.0, 1.0))
    coef = np.sum((counts - e) ** 2 / e)
    chisq_95 = 17.70

    print(f"Prueba de Uniformidad:")
    print(f"Coef = {coef:.2f}")
    print(f"Chi^2_95 = {chisq_95}")

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
        r = autocorr(x, k)
        z = r * np.sqrt(len(x))
        print(k, r, "z≈", z)


blum(prime1=383, prime2=503, seed=271)
