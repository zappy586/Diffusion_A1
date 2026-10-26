from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 15, "axes.titlesize": 16, "legend.fontsize": 12})

OUT = Path(__file__).resolve().parent.parent / "outputs"
OUT.mkdir(exist_ok=True)

THETA = 1.0
DT = 1e-3
MU0, SD0 = 3.0, 0.5
VAR0 = MU0**2 + SD0**2


def mixture_params(t, theta=THETA):
    return MU0 * np.exp(-theta * t), 1 - (1 - SD0**2) * np.exp(-2 * theta * t)


def normal_pdf(x, m, v):
    return np.exp(-((x - m) ** 2) / (2 * v)) / np.sqrt(2 * np.pi * v)


def score(x, t, theta=THETA):
    m, v = mixture_params(t, theta)
    phi1, phi2 = normal_pdf(x, -m, v), normal_pdf(x, m, v)
    w1 = phi1 / (phi1 + phi2)
    return w1 * (-(x + m) / v) + (1 - w1) * (-(x - m) / v)


def sample_p0(n, rng):
    return rng.choice([-MU0, MU0], size=n) + SD0 * rng.standard_normal(n)


def w2(a, b):
    return np.sqrt(np.mean((np.sort(a) - np.sort(b)) ** 2))


def rescaling(sigma, theta=THETA):
    return 1 / np.sqrt(1 + sigma**2), np.log(1 + sigma**2) / (2 * theta)


def shrinkage(sigma):
    return VAR0 / (VAR0 + sigma**2)


def reverse_from(x, t_start, rng, theta=THETA, dt=DT):
    steps = max(1, int(np.ceil(t_start / dt)))
    h = t_start / steps
    for k in range(steps, 0, -1):
        x = x + theta * (x + 2 * score(x, k * h, theta)) * h + np.sqrt(2 * theta * h) * rng.standard_normal(len(x))
    return x
