import matplotlib.pyplot as plt
import numpy as np

from ou import OUT, rescaling, reverse_from, sample_p0, shrinkage, w2

SIGMAS = [0.1, 0.3, 1.0, 3.0]
NS = [1_000, 5_000, 20_000]
METHODS = ["raw Y", "shrinkage", "reverse diffusion"]


def reconstruct(y, sigma, rng):
    a, t_star = rescaling(sigma)
    return {"raw Y": y, "shrinkage": shrinkage(sigma) * y, "reverse diffusion": reverse_from(a * y, t_star, rng)}


def main():
    lines = [f"{'N':>6}  {'sigma':>5}  {'t*':>6}  " + "  ".join(f"{m:>17}" for m in METHODS)]
    results = {}
    for n in NS:
        ref = sample_p0(n, np.random.default_rng(100))
        floor = w2(sample_p0(n, np.random.default_rng(7)), ref)
        for sigma in SIGMAS:
            rng = np.random.default_rng(0)
            y = sample_p0(n, rng) + sigma * rng.standard_normal(n)
            errs = {m: w2(x, ref) for m, x in reconstruct(y, sigma, rng).items()}
            results[n, sigma] = errs
            lines.append(f"{n:6d}  {sigma:5.2f}  {rescaling(sigma)[1]:6.3f}  " + "  ".join(f"{errs[m]:17.4f}" for m in METHODS))
        lines.append(f"{n:6d}  W2 between two independent p0 samples: {floor:.4f}")
    (OUT / "sensor.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))

    fig, axes = plt.subplots(1, len(NS), figsize=(18, 5), sharey=True)
    for ax, n in zip(axes, NS):
        for m, mk in zip(METHODS, ["o", "s", "^"]):
            ax.plot(SIGMAS, [results[n, s][m] for s in SIGMAS], mk + "-", ms=8, label=m)
        ax.set(xlabel=r"$\sigma_{\mathrm{sensor}}$", title=f"$N={n}$")
    axes[0].set_ylabel(r"$W_2(\hat p, p_0)$")
    axes[0].legend()
    fig.tight_layout()
    fig.savefig(OUT / "sensor_w2.png", dpi=150)


if __name__ == "__main__":
    main()
