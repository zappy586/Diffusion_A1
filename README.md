# Assignment 1: Reconstructing a State Distribution by Reverse Diffusion

MA7.510 Diffusion Models for Generative AI (Monsoon 2026)
Mohd Zeeshan, Roll no. 2025901020

## Contents

```
Diffusion_A1/
├── Report/          report.tex and the compiled report.pdf (derivations, method, results, discussion)
├── Part 1 code/     forward diffusion: sample paths, histograms, bimodality, θt collapse
├── Part 2 code/     W2 convergence, contraction bound, horizon T
├── Part 3 code/     score plots, Stein identity check
├── Part 4 code/     reverse SDE with the exact score, step size, probability flow ODE
├── Part 5 code/     imperfect score: random, bias and multiplicative errors
├── Part 6 code/     noisy sensor measurements: raw, shrinkage, reverse diffusion
├── Notes/           handwritten derivation notes
└── pyproject.toml   shared Python environment for all parts
```

Each `Part N code/` folder has `scripts/` (code), `outputs/` (all figures and numbers used in the report) and its own
`README.md` with details of the method and the outputs of each script.

**Notes:** handwritten notes for most derivations (Parts 1, 3, 4 and 5) are in the `Notes/` folder. The typed derivations in
the report are the final versions and include the corrections described there (for example the sign of the
reverse update in Part 4(b) and the restoring term in Part 5, Case B).

## Setup

Requires Python 3.10+ and [uv](https://docs.astral.sh/uv/). From the `Diffusion_A1` folder:

```bash
uv sync
```

This creates one virtual environment (`.venv`) with `numpy` and `matplotlib`, used by all parts.

## Reproducing the results

Run every command from the `Diffusion_A1` folder. Each script writes its figures and numbers to the `outputs/` folder
of its part. All scripts use fixed random seeds, so the outputs match the report.

Default parameters (from the assignment): `θ = 1`, `N = 2×10⁴`, `Δt = 10⁻³`, `T = 5.40` (computed in Part 2(d)).

### Part 1: Forward diffusion

| Task | Command | Output |
|---|---|---|
| (a) sample paths | `uv run python "Part 1 code/scripts/task_a_paths.py"` | `a_sample_paths.png` |
| (b) histograms vs exact density | `uv run python "Part 1 code/scripts/task_b_histograms.py"` | `b_histograms.png`, `b_discrepancy.txt` |
| (c) loss of bimodality | `uv run python "Part 1 code/scripts/task_c_bimodality.py"` | `c_bimodality.png`, `c_bimodality.txt` |
| (d) collapse against θt | `uv run python "Part 1 code/scripts/task_d_rescaled.py"` | `d_rescaled_time.png`, `d_rescaled.txt` |

### Part 2: Wasserstein convergence

| Task | Command | Output |
|---|---|---|
| (d) horizon T | `uv run python "Part 2 code/scripts/task_d_horizon.py"` | `d_horizon.txt` |
| (a) W2 curves | `uv run python "Part 2 code/scripts/task_a_w2_curves.py"` | `a_w2_curves.png`, `a_w2_curves.txt` |
| (b) contraction bound | `uv run python "Part 2 code/scripts/task_b_contraction.py"` | `b_contraction.png`, `b_contraction.txt` |
| (e) collapse against θt | `uv run python "Part 2 code/scripts/task_e_collapse.py"` | `e_collapse.png`, `e_collapse.txt` |

Task (c) is a proof and is in the report. `T = 5.40` from task (d) is already set in every part's `scripts/ou.py`.

### Part 3: Score and Stein identity

| Task | Command | Output |
|---|---|---|
| p_t and s_t plots | `uv run python "Part 3 code/scripts/task_score_plots.py"` | `score_plots.png` |
| Stein residuals | `uv run python "Part 3 code/scripts/task_stein.py"` | `stein.txt` |

### Part 4: Reverse diffusion with the exact score

| Task | Command | Output |
|---|---|---|
| (a, c, d) reverse SDE, moments, W2 | `uv run python "Part 4 code/scripts/task_reverse_sde.py"` | `reverse_sde_p0.png`, `reverse_sde.txt` |
| (e) step size | `uv run python "Part 4 code/scripts/task_step_size.py"` | `step_size.txt` |
| (f) probability flow ODE | `uv run python "Part 4 code/scripts/task_flow_ode.py"` | `flow_ode_vs_sde.png`, `flow_ode_vs_sde.txt` |

### Part 5: Imperfect score estimation

| Task | Command | Output |
|---|---|---|
| Cases A, B, C, W2 and D_F, plots | `uv run python "Part 5 code/scripts/task_score_errors.py"` | `w2_vs_fisher.png`, `w2_vs_parameter.png`, `score_errors.txt` |
| Case B and C predictions | `uv run python "Part 5 code/scripts/task_predictions.py"` | `predictions.txt` |

### Part 6: Noisy sensor measurements

| Task | Command | Output |
|---|---|---|
| Raw, shrinkage and reverse diffusion | `uv run python "Part 6 code/scripts/task_sensor.py"` | `sensor_w2.png`, `sensor.txt` |

### Report

The report reads its figures directly from the `outputs/` folders. To rebuild the PDF after rerunning the scripts
(requires a LaTeX installation with `pdflatex`), from the `Report` folder run `pdflatex report.tex` twice.

## Runtime

Most scripts finish in under a minute. `Part 4 code/scripts/task_step_size.py`, `Part 4 code/scripts/task_flow_ode.py`
and `Part 5 code/scripts/task_score_errors.py` run many reverse simulations and take a few minutes each.
