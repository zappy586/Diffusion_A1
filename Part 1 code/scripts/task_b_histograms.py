import matplotlib.pyplot as plt
import numpy as np

from ou import OUT, T, exact_density, simulate

TIMES = np.linspace(0, T, 5)
BINS = np.linspace(-5, 5, 101)


def discrepancy(samples, t):
    hist, edges = np.histogram(samples, bins=BINS, density=True)
    centres = 0.5 * (edges[1:] + edges[:-1])
    return np.max(np.abs(hist - exact_density(centres, t)))


def main():
    snaps, _ = simulate(TIMES)
    x = np.linspace(BINS[0], BINS[-1], 500)
    fig, axes = plt.subplots(1, len(TIMES), figsize=(4 * len(TIMES), 3.6), sharey=True)
    lines, errs = [], []
    for ax, t, s in zip(axes, TIMES, snaps):
        err = discrepancy(s, t)
        errs.append(err)
        lines.append(f"t = {t:.2f}  max |hist - p_t| = {err:.4f}")
        ax.hist(s, bins=BINS, density=True, alpha=0.5, label="Euler-Maruyama")
        ax.plot(x, exact_density(x, t), "k", lw=1.5, label="exact $p_t$")
        ax.set(title=f"$t={t:.2f}$", xlabel="$x$")
    axes[0].set_ylabel("density")
    axes[0].legend()
    fig.tight_layout()
    fig.savefig(OUT / "b_histograms.png", dpi=150)
    lines.append(f"largest discrepancy = {max(errs):.4f}")
    (OUT / "b_discrepancy.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
