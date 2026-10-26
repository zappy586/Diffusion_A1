import numpy as np

from ou import OUT, TIMES, score, simulate

TESTS = {
    "x": (lambda x: x, lambda x: np.ones_like(x)),
    "x^2": (lambda x: x**2, lambda x: 2 * x),
    "sin(x)": (np.sin, np.cos),
    "exp(-x^2/2)": (lambda x: np.exp(-(x**2) / 2), lambda x: -x * np.exp(-(x**2) / 2)),
}


def stein_check(x, t, f, df):
    terms = df(x) + f(x) * score(x, t)
    return abs(terms.mean()), terms.std(ddof=1) / np.sqrt(len(x))


def main():
    lines = [f"{'t':>5}  {'f':<12} {'R_f':>9} {'SE':>9} {'R_f/SE':>7}  pass"]
    for t, x in zip(TIMES, simulate(TIMES)):
        for name, (f, df) in TESTS.items():
            r, se = stein_check(x, t, f, df)
            lines.append(f"{t:5.2f}  {name:<12} {r:9.5f} {se:9.5f} {r / se:7.2f}  {'yes' if r <= 2 * se else 'no'}")
    (OUT / "stein.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
