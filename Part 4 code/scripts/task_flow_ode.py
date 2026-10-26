import matplotlib.pyplot as plt

from ou import OUT, reference_p0, reverse, w2

DTS = [0.2, 0.1, 0.05, 0.025, 0.0125, 0.005, 0.001]


def main():
    ref = reference_p0()
    sde = [w2(reverse(dt), ref) for dt in DTS]
    ode = [w2(reverse(dt, ode=True), ref) for dt in DTS]
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(DTS, sde, "o-", label="reverse SDE")
    ax.plot(DTS, ode, "s-", label="probability flow ODE")
    ax.set(xlabel=r"$\Delta t$", ylabel=r"$W_2(\hat p_0, p_0)$", title="Reverse SDE vs probability flow ODE")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "flow_ode_vs_sde.png", dpi=150)
    lines = [f"{'dt':>7}  {'SDE':>7}  {'ODE':>7}"] + [f"{dt:7.4f}  {a:7.4f}  {b:7.4f}" for dt, a, b in zip(DTS, sde, ode)]
    (OUT / "flow_ode_vs_sde.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
