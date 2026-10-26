import matplotlib.pyplot as plt
import numpy as np

from ou import OUT, bimodal_threshold, count_modes, exact_density

GRID = np.linspace(-6, 6, 4001)


def numerical_threshold(dt=1e-4):
    t = 0.0
    while count_modes(exact_density(GRID, t)) > 1:
        t += dt
    return t


def main():
    t_star = bimodal_threshold()
    t_num = numerical_threshold()
    fig, ax = plt.subplots(figsize=(9, 5))
    x = np.linspace(-5, 5, 500)
    for t in [0, 0.5, 0.9, t_star, 1.5, 3.0]:
        ax.plot(x, exact_density(x, t), label=f"$t={t:.3f}$")
    ax.set(xlabel="$x$", ylabel="$p_t(x)$", title="Exact density $p_t$")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "c_bimodality.png", dpi=150)
    lines = [
        f"analytic threshold t* = ln(9.75)/(2 theta) = {t_star:.5f}",
        f"numerical threshold (first t with one mode on grid) = {t_num:.5f}",
    ]
    (OUT / "c_bimodality.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
