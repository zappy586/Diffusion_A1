import numpy as np

from ou import DT, OUT, reference_p0, reverse, w2

DTS = [DT, DT / 2, DT / 4]


def main():
    ref = reference_p0()
    errs = [w2(reverse(dt), ref) for dt in DTS]
    lines = [f"{'dt':>9}  {'W2(p0_hat, p0)':>14}"]
    lines += [f"{dt:9.5f}  {e:14.4f}" for dt, e in zip(DTS, errs)]
    lines += [f"observed order: {', '.join(f'{np.log2(a / b):.2f}' for a, b in zip(errs, errs[1:]))}"]
    (OUT / "step_size.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
