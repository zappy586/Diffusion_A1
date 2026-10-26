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
EPS = 1e-2
MU0, SD0 = 3.0, 0.5


def w2(a, b):
    return np.sqrt(np.mean((np.sort(a) - np.sort(b)) ** 2))


def sample_p0(n, rng):
    return rng.choice([-MU0, MU0], size=n) + SD0 * rng.standard_normal(n)


def sample_pi(n, rng):
    return rng.standard_normal(n)


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


def w2_p0_pi(seed=1):
    rng = np.random.default_rng(seed)
    return w2(sample_p0(N, rng), sample_pi(N, rng))
