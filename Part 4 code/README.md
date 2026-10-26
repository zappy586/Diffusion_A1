# Part 4: Reverse Diffusion with the Exact Score

Runs the reverse-time OU process from `T` down to `0`, starting from `π = N(0, 1)`, using the exact
score from Part 3, and compares the result `p̂0` with `p0`. Also compares the reverse SDE with the
probability flow ODE.

## Layout

```
Part 4 code/
├── scripts/
│   ├── ou.py                 parameters, density, exact score, reverse SDE / ODE, W2
│   ├── task_reverse_sde.py   (a, c, d) reverse SDE at Δt = 1e-3, histogram, moments, W2
│   ├── task_step_size.py     (e) W2(p̂0, p0) for Δt, Δt/2, Δt/4
│   └── task_flow_ode.py      (f) W2(p̂0, p0) for the reverse SDE and the probability flow ODE
└── outputs/                  figures (.png) and numbers (.txt)
```

## Method

- **Reverse SDE:** `X ← X + θ(X + 2 s_t(X)) Δt + sqrt(2θΔt) Z`, stepping `t = T, T − Δt, …, Δt`.
  (The assignment's equation (9) prints `−2θ s_t`; the correct sign is `+`, see the report, Part 4(b).)
- **Probability flow ODE:** `X ← X + θ(X + s_t(X)) Δt`.
- **Start:** `N = 2×10⁴` samples from `π` instead of `p_T`.
- **W2:** sorted-sample estimator against a fixed sample of `N` points from `p0`.
- **Step sizes:** (e) uses `Δt ∈ {1e-3, 5e-4, 2.5e-4}`; (f) uses `Δt ∈ {0.2, 0.1, 0.05, 0.025, 0.0125, 0.005, 0.001}`.
- Defaults: `θ = 1`, `N = 2×10⁴`, `Δt = 10⁻³`, `T = 5.40` (from Part 2(d)), seed `0`.

## Reproducing

Requires [uv](https://docs.astral.sh/uv/). All parts share one environment, defined by `pyproject.toml` in the
top-level `Diffusion_A1` folder. From that folder:

```bash
uv sync
```

```bash
uv run python "Part 4 code/scripts/task_reverse_sde.py"
```

```bash
uv run python "Part 4 code/scripts/task_step_size.py"
```

```bash
uv run python "Part 4 code/scripts/task_flow_ode.py"
```

| Script | Outputs |
|---|---|
| `task_reverse_sde.py` | `reverse_sde_p0.png`, `reverse_sde.txt` |
| `task_step_size.py` | `step_size.txt` |
| `task_flow_ode.py` | `flow_ode_vs_sde.png`, `flow_ode_vs_sde.txt` |
