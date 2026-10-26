import matplotlib.pyplot as plt
import numpy as np

from ou import OUT, T, density, score

PLOT_TIMES = [0, 0.5, 1.0, 2.0, T]


def main():
    x = np.linspace(-6, 6, 1001)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    for t in PLOT_TIMES:
        ax1.plot(x, density(x, t), label=f"$t={t:.2f}$")
        ax2.plot(x, score(x, t), label=f"$t={t:.2f}$")
    ax2.plot(x, -x, "k--", lw=1, label=r"$-x$ (score of $\pi$)")
    ax1.set(xlabel="$x$", ylabel="$p_t(x)$", title="Density $p_t$")
    ax2.set(xlabel="$x$", ylabel="$s_t(x)$", title="Score $s_t$", ylim=(-15, 15))
    ax1.legend()
    ax2.legend()
    fig.tight_layout()
    fig.savefig(OUT / "score_plots.png", dpi=150)


if __name__ == "__main__":
    main()
