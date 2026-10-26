import matplotlib.pyplot as plt

from ou import OUT
from task_a_w2_curves import TIMES, w2_curves

THETAS = [0.5, 1.0, 2.0]
MARKERS = ["o", "s", "^"]


def main():
    fig, ax = plt.subplots(figsize=(9, 5))
    lines = ["theta  theta*t  W2(pt,pi)  W2(pt,p0)"]
    for theta, mk in zip(THETAS, MARKERS):
        to_pi, to_p0 = w2_curves(TIMES / theta, theta=theta)
        ax.plot(TIMES, to_pi, mk, ms=5, mfc="none", c="C0", label=rf"$W_2(p_t,\pi)$, $\theta={theta}$")
        ax.plot(TIMES, to_p0, mk, ms=5, mfc="none", c="C1", label=rf"$W_2(p_t,p_0)$, $\theta={theta}$")
        lines += [f"{theta:5.1f}  {s:7.3f}  {a:.4f}     {b:.4f}" for s, a, b in zip(TIMES, to_pi, to_p0)]
    ax.set(xlabel=r"$\theta t$", ylabel="$W_2$", title=r"Collapse against rescaled time $\theta t$")
    ax.legend(fontsize=10, ncol=2)
    fig.tight_layout()
    fig.savefig(OUT / "e_collapse.png", dpi=150)
    (OUT / "e_collapse.txt").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
