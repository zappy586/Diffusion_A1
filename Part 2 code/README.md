# Part 2: Convergence to Equilibrium in Wasserstein Distance

Estimates `W2` between the OU marginals `p_t`, the initial law `p0` and the stationary law
`π = N(0, 1)`, checks the contraction bound `W2(p_t, π) ≤ e^{-θt} W2(p0, π)`, and sets the horizon `T`.

## Layout

```
Part 2 code/
├── scripts/
│   ├── ou.py                 parameters, sampler, Euler–Maruyama, W2 estimator
│   ├── task_a_w2_curves.py   (a) W2(p_t, π) and W2(p_t, p0) over [0, T]
│   ├── task_b_contraction.py (b) W2(p0, π) and the contraction bound
│   ├── task_d_horizon.py     (d) smallest T with bound ≤ 1e-2
│   └── task_e_collapse.py    (e) θ ∈ {0.5, 1, 2} against θt
└── outputs/                  figures (.png) and numbers (.txt)
```

## Method

- **W2 estimate:** sort both sample sets (each of size `N = 2×10⁴`) and take the root mean squared
  difference of matched order statistics. `p_t` samples come from the Euler–Maruyama simulation;
  the reference `π` and `p0` samples are drawn independently.
- Defaults: `θ = 1`, `N = 2×10⁴`, `Δt = 10⁻³`, simulation seed `0`.

## Reproducing

Requires [uv](https://docs.astral.sh/uv/). All parts share one environment, defined by `pyproject.toml` in the
top-level `Diffusion_A1` folder. From that folder:

```bash
uv sync
```

Run task (d) first, since it determines `T`. `T = 5.40` is already set in the `ou.py` of
Parts 1, 2 and 3.

```bash
uv run python "Part 2 code/scripts/task_d_horizon.py"
```

```bash
uv run python "Part 2 code/scripts/task_a_w2_curves.py"
```

```bash
uv run python "Part 2 code/scripts/task_b_contraction.py"
```

```bash
uv run python "Part 2 code/scripts/task_e_collapse.py"
```

| Script | Outputs |
|---|---|
| `task_d_horizon.py` | `d_horizon.txt` |
| `task_a_w2_curves.py` | `a_w2_curves.png`, `a_w2_curves.txt` |
| `task_b_contraction.py` | `b_contraction.png`, `b_contraction.txt` |
| `task_e_collapse.py` | `e_collapse.png`, `e_collapse.txt` |

Task (c) is a proof and is in the report.
