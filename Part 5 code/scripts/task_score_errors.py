import matplotlib.pyplot as plt
import numpy as np

from ou import OUT, T, fisher_divergence, forward, reference_p0, reverse, score, w2

GRID = np.linspace(-6, 6, 200)
SIGMAS = [0.1, 0.3, 1.0, 3.0]
CS = [-1.0, -0.5, -0.2, 0.2, 0.5, 1.0]
ALPHAS = [-0.5, -0.25, -0.1, 0.1, 0.25, 0.5]
TIMES = np.round(np.linspace(0, T, 55), 3)


def random_error(sigma, seed=1):
    e = np.random.default_rng(seed).normal(0, sigma, len(GRID))
    return lambda x, t: score(x, t) + np.interp(x, GRID, e)


def bias(c):
    return lambda x, t: score(x, t) + c


def scale(alpha):
    return lambda x, t: (1 + alpha) * score(x, t)


CASES = {
    "A": ("random error", r"$\sigma_\epsilon$", SIGMAS, random_error, "o"),
    "B": ("constant bias", "$c$", CS, bias, "s"),
    "C": ("multiplicative error", r"$\alpha$", ALPHAS, scale, "^"),
}


def run_all():
    ref = reference_p0()
    snaps = forward(TIMES)
    results = {}
    for key, (_, _, params, make, _) in CASES.items():
        rows = []
        for p in params:
            s_hat = make(p)
            x = reverse(s_hat)
            rows.append((p, w2(x, ref), fisher_divergence(s_hat, TIMES, snaps), x.mean(), x.var()))
        results[key] = rows
    return results


def plot(results):
    fig, ax = plt.subplots(figsize=(9, 5.5))
    for key, (name, _, _, _, mk) in CASES.items():
        r = np.array(results[key])
        ax.plot(r[:, 2], r[:, 1], mk, ms=8, label=f"Case {key}: {name}")
    ax.set(xlabel=r"$D_F$", ylabel=r"$W_2(\hat p_0, p_0)$", title="Reconstruction error against Fisher divergence")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "w2_vs_fisher.png", dpi=150)

    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    for ax, (key, (name, sym, _, _, mk)) in zip(axes, CASES.items()):
        r = np.array(results[key])
        ax.plot(r[:, 0], r[:, 1], mk + "-", ms=8)
        ax.set(xlabel=sym, ylabel=r"$W_2(\hat p_0, p_0)$", title=f"Case {key}: {name}")
    fig.tight_layout()
    fig.savefig(OUT / "w2_vs_parameter.png", dpi=150)


def main():
    results = run_all()
    plot(results)
    lines = []
    for key, (name, _, _, _, _) in CASES.items():
        lines += [f"Case {key}: {name}", f"{'param':>7}  {'W2':>7}  {'D_F':>9}  {'mean':>8}  {'var':>8}"]
        lines += [f"{p:7.2f}  {a:7.4f}  {d:9.4f}  {m:8.4f}  {v:8.4f}" for p, a, d, m, v in results[key]]
        lines.append("")
    (OUT / "score_errors.txt").write_text("\n".join(lines))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
