import matplotlib.pyplot as plt
import numpy as np

from ou import OUT, THETA, w2_p0_pi
from task_a_w2_curves import TIMES, w2_curves


def main():
    w0 = w2_p0_pi()
    est, _ = w2_curves(TIMES)
    bound = np.exp(-THETA * TIMES) * w0

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(TIMES, bound, "k--", label=r"bound $e^{-\theta t}W_2(p_0,\pi)$")
    ax.plot(TIMES, est, "o", ms=4, label=r"$W_2(p_t,\pi)$ estimate")
    ax.set(xlabel="$t$", ylabel=r"$W_2(p_t,\pi)$", title="Contraction bound")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "b_contraction.png", dpi=150)

    lines = [f"W2(p0, pi) = {w0:.5f}", "     t  estimate   bound   bound/estimate"]
    lines += [f"{t:6.3f}  {e:.5f}  {b:.5f}  {b / e:7.2f}" for t, e, b in zip(TIMES, est, bound)]
    (OUT / "b_contraction.txt").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
