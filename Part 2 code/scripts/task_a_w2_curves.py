import matplotlib.pyplot as plt
import numpy as np

from ou import N, OUT, T, THETA, sample_p0, sample_pi, simulate, w2

TIMES = np.round(np.linspace(0, T, 55), 3)


def w2_curves(times, theta=THETA, seed=0):
    rng = np.random.default_rng(seed + 100)
    ref_pi, ref_p0 = sample_pi(N, rng), sample_p0(N, rng)
    snaps = simulate(times, theta=theta, seed=seed)
    return np.array([w2(s, ref_pi) for s in snaps]), np.array([w2(s, ref_p0) for s in snaps])


def main():
    to_pi, to_p0 = w2_curves(TIMES)
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(TIMES, to_pi, "o-", ms=4, label=r"$W_2(p_t,\pi)$")
    ax.plot(TIMES, to_p0, "s-", ms=4, label=r"$W_2(p_t,p_0)$")
    ax.set(xlabel="$t$", ylabel="$W_2$", title=rf"Wasserstein distances, $\theta={THETA}$")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "a_w2_curves.png", dpi=150)
    rows = [f"{t:6.3f}  {a:.4f}  {b:.4f}" for t, a, b in zip(TIMES, to_pi, to_p0)]
    (OUT / "a_w2_curves.txt").write_text("\n".join(["     t  W2(pt,pi)  W2(pt,p0)", *rows]) + "\n")


if __name__ == "__main__":
    main()
