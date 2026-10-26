import matplotlib.pyplot as plt
import numpy as np

from ou import OUT, T, exact_density, simulate
from task_b_histograms import BINS, discrepancy

THETAS = [0.5, 1.0, 2.0]
S = np.linspace(0, T, 5)


def main():
    x = np.linspace(BINS[0], BINS[-1], 500)
    fig, axes = plt.subplots(1, len(S), figsize=(4 * len(S), 3.6), sharey=True)
    lines = []
    for theta in THETAS:
        snaps, _ = simulate(S / theta, theta=theta)
        for ax, s, samples in zip(axes, S, snaps):
            ax.hist(samples, bins=BINS, density=True, histtype="step", lw=1.2, label=f"$\\theta={theta}$")
            lines.append(f"theta = {theta}  theta*t = {s:.2f}  max |hist - p| = {discrepancy(samples, s):.4f}")
    for ax, s in zip(axes, S):
        ax.plot(x, exact_density(x, s), "k", lw=1, label="exact ($\\theta t$)")
        ax.set(title=f"$\\theta t={s:.2f}$", xlabel="$x$")
    axes[0].set_ylabel("density")
    axes[0].legend()
    fig.tight_layout()
    fig.savefig(OUT / "d_rescaled_time.png", dpi=150)
    (OUT / "d_rescaled.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
