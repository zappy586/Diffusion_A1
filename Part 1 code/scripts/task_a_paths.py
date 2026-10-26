import matplotlib.pyplot as plt
import numpy as np

from ou import DT, OUT, T, simulate


def main(n_paths=10, seed=6):
    _, paths = simulate([T], n=n_paths, seed=seed, keep=n_paths)
    t = np.arange(paths.shape[0]) * DT
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(t, paths, lw=0.8)
    ax.set(xlabel="$t$", ylabel="$X_t$", title=f"{n_paths} sample paths of the OU process ($\\theta=1$)")
    fig.tight_layout()
    fig.savefig(OUT / "a_sample_paths.png", dpi=150)


if __name__ == "__main__":
    main()
