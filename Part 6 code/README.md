# Part 6: Noisy Sensor Measurements

Reconstructs `p0` from noisy observations `Y = X0 + η`, `η ~ N(0, σ²)`, in three ways, and compares them by
`W2(p̂, p0)` over several sensor noise levels `σ` and sample sizes `N`.

## Layout

```
Part 6 code/
├── scripts/
│   ├── ou.py            parameters, exact score, rescaling (a, t*), shrinkage λ, reverse SDE, W2
│   └── task_sensor.py   runs the three reconstructions for every (N, σ), writes the table and plot
└── outputs/             figures (.png) and numbers (.txt)
```

## Method

- **Raw:** use `Y` directly.
- **Shrinkage:** `λY` with `λ = 9.25 / (9.25 + σ²)` (MSE-optimal when `X0` is treated as Gaussian with mean `0`, variance `9.25`).
- **Reverse diffusion:** start at `X_{t*} = aY` with `a = 1/sqrt(1 + σ²)`, `t* = ln(1 + σ²)/(2θ)`, and integrate the reverse SDE
  with the exact score down to `t = 0`, using steps of `t*/ceil(t*/1e-3) ≤ 1e-3`.
- `σ ∈ {0.1, 0.3, 1, 3}`, `N ∈ {1000, 5000, 20000}`, `θ = 1`, one run per `(N, σ)`.
- **W2:** sorted-sample estimator against a fixed sample of `N` points from `p0`.

## Reproducing

Requires [uv](https://docs.astral.sh/uv/). All parts share one environment, defined by `pyproject.toml` in the
top-level `Diffusion_A1` folder. From that folder:

```bash
uv sync
```

```bash
uv run python "Part 6 code/scripts/task_sensor.py"
```

| Script | Outputs |
|---|---|
| `task_sensor.py` | `sensor_w2.png`, `sensor.txt` |
