from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 15, "axes.titlesize": 16, "legend.fontsize": 12})

OUT = Path(__file__).resolve().parent.parent / "outputs"
OUT.mkdir(exist_ok=True)

THETA = 1.0
N = 20_000
DT = 1e-3
T = 5.40
MU0, SD0 = 3.0, 0.5


def mixture_params(t, theta=THETA):
    return MU0 * np.exp(-theta * t), 1 - (1 - SD0**2) * np.exp(-2 * theta * t)


def normal_pdf(x, m, v):
    return np.exp(-((x - m) ** 2) / (2 * v)) / np.sqrt(2 * np.pi * v)


def density(x, t, theta=THETA):
    m, v = mixture_params(t, theta)
    return 0.5 * normal_pdf(x, -m, v) + 0.5 * normal_pdf(x, m, v)


def score(x, t, theta=THETA):
    m, v = mixture_params(t, theta)
    phi1, phi2 = normal_pdf(x, -m, v), normal_pdf(x, m, v)
    w1 = phi1 / (phi1 + phi2)
    return w1 * (-(x + m) / v) + (1 - w1) * (-(x - m) / v)


def sample_p0(n, rng):
    return rng.choice([-MU0, MU0], size=n) + SD0 * rng.standard_normal(n)


def reference_p0(seed=100):
    return sample_p0(N, np.random.default_rng(seed))


def w2(a, b):
    return np.sqrt(np.mean((np.sort(a) - np.sort(b)) ** 2))


def reverse(dt, ode=False, theta=THETA, seed=0):
    rng = np.random.default_rng(seed)
    x = rng.standard_normal(N)
    for k in range(int(round(T / dt)), 0, -1):
        s = score(x, k * dt, theta)
        if ode:
            x = x + theta * (x + s) * dt
        else:
            x = x + theta * (x + 2 * s) * dt + np.sqrt(2 * theta * dt) * rng.standard_normal(N)
    return x
