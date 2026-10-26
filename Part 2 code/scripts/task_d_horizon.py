import numpy as np

from ou import EPS, OUT, THETA, w2_p0_pi


def main():
    w0 = w2_p0_pi()
    t = np.log(w0 / EPS) / THETA
    lines = [
        f"W2(p0, pi) = {w0:.5f}",
        f"T = ln(W2(p0, pi) / {EPS}) / theta = {t:.5f}",
        f"T used (rounded up) = {np.ceil(t * 100) / 100:.2f}",
    ]
    (OUT / "d_horizon.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
