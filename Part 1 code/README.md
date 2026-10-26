# Part 1: Simulating the Forward Diffusion

Euler–Maruyama simulation of the OU process `dX = -θX dt + sqrt(2θ) dW` started from the
two-mode mixture `p0 = ½N(-3, 0.5²) + ½N(3, 0.5²)`, compared against the exact density `p_t`.

## Layout

```
Part 1 code/
├── scripts/
│   ├── ou.py                  shared parameters, exact density, sampler, Euler–Maruyama
│   ├── task_a_paths.py        (a) sample paths
│   ├── task_b_histograms.py   (b) histograms vs exact density + largest discrepancy
│   ├── task_c_bimodality.py   (c) loss of bimodality, analytic and numerical threshold
│   └── task_d_rescaled.py     (d) θ ∈ {0.5, 1, 2} against rescaled time θt
└── outputs/                   figures (.png) and numbers (.txt)
```

## Parameters

Defaults from Table 1: `θ = 1`, `N = 2×10⁴`, `Δt = 10⁻³`, seed `0`, all set in `scripts/ou.py`.
The sample-path figure (task a) uses seed `6`: with seed `0` one of the ten plotted paths makes a
rare excursion to about −5 that distracts from the typical behaviour.
The horizon `T = 5.40` comes from Part 2(d) (see `Part 2 code/outputs/d_horizon.txt`).

## Reproducing

Requires [uv](https://docs.astral.sh/uv/). All parts share one environment, defined by `pyproject.toml` in the
top-level `Diffusion_A1` folder. From that folder:

```bash
uv sync
```

```bash
uv run python "Part 1 code/scripts/task_a_paths.py"
```

```bash
uv run python "Part 1 code/scripts/task_b_histograms.py"
```

```bash
uv run python "Part 1 code/scripts/task_c_bimodality.py"
```

```bash
uv run python "Part 1 code/scripts/task_d_rescaled.py"
```

| Script | Outputs |
|---|---|
| `task_a_paths.py` | `a_sample_paths.png` |
| `task_b_histograms.py` | `b_histograms.png`, `b_discrepancy.txt` |
| `task_c_bimodality.py` | `c_bimodality.png`, `c_bimodality.txt` |
| `task_d_rescaled.py` | `d_rescaled_time.png`, `d_rescaled.txt` |

Results are deterministic for a fixed seed.

## Notes on the measures used

- **Discrepancy (b, d):** largest absolute gap between the normalised histogram (100 bins on
  `[-5, 5]`) and `p_t` at the bin centres.
- **Bimodality (c):** `p_t` is a symmetric mixture of two Gaussians with equal variance `v_t` and
  means `±3e^{-θt}`. It is bimodal iff `9e^{-2θt} > v_t`, giving `t* = ln(9.75)/(2θ)`.
  The script checks this by counting local maxima of `p_t` on a fine grid.
