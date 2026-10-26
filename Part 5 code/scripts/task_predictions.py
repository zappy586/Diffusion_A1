import numpy as np

from ou import MU0, OUT, SD0, T, THETA, mixture_params

ALPHAS = [-0.25, -0.1, 0.1, 0.25, 0.5]


def bias_shift_per_unit_c():
    s = np.linspace(0, T, 200_001)
    v = mixture_params(s)[1]
    return 2 * THETA * SD0**2 * np.trapezoid(np.exp(-THETA * s) / v, s)


def main():
    lines = [f"Case B: predicted mean shift delta_0 = {bias_shift_per_unit_c():.4f} * c", "",
             "Case C: predicted variance 9 + v0/(1+2 alpha)"]
    lines += [f"alpha = {a:5.2f}  within-mode {SD0**2 / (1 + 2 * a):.4f}  total {MU0**2 + SD0**2 / (1 + 2 * a):.4f}" for a in ALPHAS]
    (OUT / "predictions.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
