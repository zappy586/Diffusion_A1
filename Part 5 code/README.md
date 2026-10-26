# Part 5: Effect of Imperfect Score Estimation

Repeats the Part 4 reverse-SDE reconstruction with an estimated score `ŝ_t` in place of the exact score,
for three error models, and records the reconstruction error `W2(p̂0, p0)` and the Fisher divergence `D_F`.

## Layout

```
Part 5 code/
├── scripts/
│   ├── ou.py                 parameters, exact score, forward and reverse simulation, W2, D_F
│   └── task_score_errors.py  runs cases A, B, C, writes the table and both plots
└── outputs/                  figures (.png) and numbers (.txt)
```

## Method

- **Reverse SDE:** `X ← X + θ(X + 2 ŝ_t(X)) Δt + sqrt(2θΔt) Z` from `T` down to `0`, starting from `N` samples of `π`
  (corrected sign of the assignment's equation (9), see the report, Part 4(b)).
- **Case A (random error):** `ŝ_t = s_t + e`, with `e` the linear interpolation of `e_k ~ N(0, σ²)` drawn once on
  `K = 200` grid points in `[−6, 6]` and held fixed for the whole run. `σ ∈ {0.1, 0.3, 1, 3}`.
- **Case B (constant bias):** `ŝ_t = s_t + c`, `c ∈ {±0.2, ±0.5, ±1}`.
- **Case C (multiplicative error):** `ŝ_t = (1 + α) s_t`, `α ∈ {±0.1, ±0.25, ±0.5}`.
- **W2:** sorted-sample estimator against a fixed sample of `N` points from `p0`.
- **D_F:** mean of `(ŝ_t − s_t)²` over the Part 1 forward particles at 55 equally spaced times in `[0, T]`,
  integrated over time with the trapezoidal rule and divided by `T`.
- Defaults: `θ = 1`, `N = 2×10⁴`, `Δt = 10⁻³`, `T = 5.40` (from Part 2(d)), seed `0`.

## Reproducing

Requires [uv](https://docs.astral.sh/uv/). All parts share one environment, defined by `pyproject.toml` in the
top-level `Diffusion_A1` folder. From that folder:

```bash
uv sync
```

```bash
uv run python "Part 5 code/scripts/task_score_errors.py"
```

| Script | Outputs |
|---|---|
| `task_score_errors.py` | `w2_vs_fisher.png`, `w2_vs_parameter.png`, `score_errors.txt` |
