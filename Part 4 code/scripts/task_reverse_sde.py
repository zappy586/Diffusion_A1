import matplotlib.pyplot as plt
import numpy as np

from ou import DT, MU0, OUT, SD0, density, reference_p0, reverse, w2


def main():
    x = reverse(DT)
    ref = reference_p0()
    grid = np.linspace(-5, 5, 500)
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.hist(x, bins=np.linspace(-5, 5, 101), density=True, alpha=0.5, label=r"$\hat p_0$ (reverse SDE)")
    ax.plot(grid, density(grid, 0.0), "k", lw=1.5, label="$p_0$")
    ax.set(xlabel="$x$", ylabel="density", title=rf"Reconstructed $\hat p_0$, $\Delta t={DT}$")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "reverse_sde_p0.png", dpi=150)
    lines = [
        f"mean      p0_hat = {x.mean():.4f}   p0 = 0",
        f"variance  p0_hat = {x.var():.4f}   p0 = {MU0**2 + SD0**2:.4f}",
        f"W2(p0_hat, p0)   = {w2(x, ref):.4f}",
        f"W2 between two independent p0 samples = {w2(reference_p0(seed=7), ref):.4f}",
    ]
    (OUT / "reverse_sde.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
