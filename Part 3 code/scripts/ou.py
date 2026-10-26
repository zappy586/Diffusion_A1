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
TIMES = np.round(np.linspace(0, T, 5), 3)


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


def simulate(times, theta=THETA, n=N, dt=DT, seed=0):
    rng = np.random.default_rng(seed)
    x = sample_p0(n, rng)
    steps = np.rint(np.asarray(times) / dt).astype(int)
    wanted = set(steps.tolist())
    snaps = {0: x.copy()}
    for k in range(1, steps.max() + 1):
        x = x - theta * x * dt + np.sqrt(2 * theta * dt) * rng.standard_normal(n)
        if k in wanted:
            snaps[k] = x.copy()
    return [snaps[s] for s in steps]
