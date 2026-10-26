# Part 3: Score Function and the Stein Identity

Plots the density `p_t` and its score `s_t(x) = ∂ₓ log p_t(x)`, and checks the Stein identity
`E[f'(X)] = −E[f(X) s_t(X)]` on samples from the forward simulation.

## Layout

```
Part 3 code/
├── scripts/
│   ├── ou.py                 parameters, density, closed-form score, Euler–Maruyama
│   ├── task_score_plots.py   p_t and s_t at t ∈ {0, 0.5, 1, 2, T}
│   └── task_stein.py         Stein residuals and standard errors for four test functions
└── outputs/                  figures (.png) and numbers (.txt)
```

## Method

- **Score:** `s_t(x) = w₁ s₁ + w₂ s₂`, the weighted average of the component scores `s₁ = −(x + m_t)/v_t`, `s₂ = −(x − m_t)/v_t`, with weights `w_k = φ_k / (φ₁ + φ₂)`; `m_t = 3e^{−θt}`, `v_t = 1 − 0.75e^{−2θt}`
  (derived in the report, Part 3(b)).
- **Stein check:** at `t ∈ {0, 1.35, 2.70, 4.05, 5.40}`, take the `N = 2×10⁴` simulated particles, compute
  `R_f = |mean(f'(X) + f(X) s_t(X))|` and `SE = std(f'(X) + f(X) s_t(X)) / sqrt(N)`. A check passes when `R_f ≤ 2 SE`.
- Test functions: `x`, `x²`, `sin(x)`, `exp(−x²/2)`.
- Defaults: `θ = 1`, `N = 2×10⁴`, `Δt = 10⁻³`, `T = 5.40` (from Part 2(d)), seed `0`.

## Reproducing

Requires [uv](https://docs.astral.sh/uv/). All parts share one environment, defined by `pyproject.toml` in the
top-level `Diffusion_A1` folder. From that folder:

```bash
uv sync
```

```bash
uv run python "Part 3 code/scripts/task_score_plots.py"
```

```bash
uv run python "Part 3 code/scripts/task_stein.py"
```

| Script | Outputs |
|---|---|
| `task_score_plots.py` | `score_plots.png` |
| `task_stein.py` | `stein.txt` |
