import matplotlib.pyplot as plt
import numpy as np

WORD_SIZE = 32
STATE_SIZE = 624
MIDDLE = 397
SEPARATION_BIT = 31
MATRIX_A = 0x9908B0DF
SHIFT_U = 11
MASK_D = 0xFFFFFFFF
SHIFT_S = 7
MASK_B = 0x9D2C5680
SHIFT_T = 15
MASK_C = 0xEFC60000
SHIFT_L = 18
INIT_MULT = 1812433253
LOWER_MASK = (1 << SEPARATION_BIT) - 1
UPPER_MASK = (~LOWER_MASK) & 0xFFFFFFFF

container = {
    "state": [0] * STATE_SIZE,
    "index": STATE_SIZE,
}


def seed_mt(seed):
    seed &= 0xFFFFFFFF
    S = container["state"]
    S[0] = seed
    for i in range(1, STATE_SIZE):
        prev = S[i - 1] ^ (S[i - 1] >> 30)
        S[i] = (INIT_MULT * prev + i) & 0xFFFFFFFF
    container["index"] = STATE_SIZE


def twist():
    S = container["state"]
    for i in range(STATE_SIZE):
        bits = (S[i] & UPPER_MASK) | (S[(i + 1) % STATE_SIZE] & LOWER_MASK)
        bitsA = bits >> 1
        if bits & 1:
            bitsA ^= MATRIX_A
        S[i] = (S[(i + MIDDLE) % STATE_SIZE] ^ bitsA) & 0xFFFFFFFF
    container["index"] = 0


def mersenne_twister():
    if container["index"] >= STATE_SIZE:
        twist()
    S = container["state"]
    idx = container["index"]
    y = S[idx]
    container["index"] = idx + 1
    y ^= (y >> SHIFT_U) & MASK_D
    y ^= (y << SHIFT_S) & MASK_B
    y ^= (y << SHIFT_T) & MASK_C
    y ^= y >> SHIFT_L
    return y & 0xFFFFFFFF


def mersenne_twister_histogram(seed):
    numbers = []
    seed_mt(seed)
    for _ in range(10000):
        numbers.append(mersenne_twister())
    normalized = [x / 4294967296.0 for x in numbers]

    plt.hist(normalized, bins=30, edgecolor="black", linewidth=1.2)
    plt.title("Mersenne Twister Histogram")
    plt.xlabel("Generated Number")
    plt.ylabel("Frequency")
    plt.grid(True, alpha=0.3)
    plt.savefig("histograms/mersenne_twister_hist.png")
    plt.close()

    print("=== Pruebas de Hipótesis ===")

    bins = 30
    n = len(normalized)
    e = n / bins
    counts, _ = np.histogram(normalized, bins=bins, range=(0.0, 1.0))
    coef = np.sum((counts - e) ** 2 / e)
    chisq_95 = 17.70

    print(f"Prueba de Uniformidad:")
    print(f"Coef = {coef:.2f}")
    print(f"Chi^2_95 = {chisq_95}")

    def autocorr(x, k):
        x = np.asarray(x)
        xbar = x.mean()
        num = np.dot(x[: n - k] - xbar, x[k:] - xbar)
        den = np.dot(x - xbar, x - xbar)
        return num / den

    print(f"\nPrueba de Independencia:")
    x = np.array(normalized).reshape(-1)

    for k in (1, 2, 3, 4, 5):
        r = autocorr(x, k)
        z = r * np.sqrt(len(x))
        print(k, r, "z≈", z)


mersenne_twister_histogram(3944)
