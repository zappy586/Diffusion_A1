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


def normal_pdf(x, m, v):
    return np.exp(-((x - m) ** 2) / (2 * v)) / np.sqrt(2 * np.pi * v)


def exact_density(x, t, theta=THETA):
    m = MU0 * np.exp(-theta * t)
    v = 1 - (1 - SD0**2) * np.exp(-2 * theta * t)
    return 0.5 * normal_pdf(x, -m, v) + 0.5 * normal_pdf(x, m, v)


def sample_p0(n, rng):
    return rng.choice([-MU0, MU0], size=n) + SD0 * rng.standard_normal(n)


def simulate(times, theta=THETA, n=N, dt=DT, seed=0, keep=0):
    rng = np.random.default_rng(seed)
    x = sample_p0(n, rng)
    steps = np.rint(np.asarray(times) / dt).astype(int)
    total = steps.max()
    snaps = {0: x.copy()} if 0 in steps else {}
    paths = np.empty((total + 1, keep))
    paths[0] = x[:keep]
    noise = np.sqrt(2 * theta * dt)
    for k in range(1, total + 1):
        x = x - theta * x * dt + noise * rng.standard_normal(n)
        paths[k] = x[:keep]
        if k in steps:
            snaps[k] = x.copy()
    return [snaps[s] for s in steps], paths


def count_modes(f):
    return int(np.sum((f[1:-1] > f[:-2]) & (f[1:-1] > f[2:])))


def bimodal_threshold(theta=THETA):
    return np.log(MU0**2 + 1 - SD0**2) / (2 * theta)
