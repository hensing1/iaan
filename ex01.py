import math
from matplotlib import pyplot as plt
import numpy as np

N = 5


def euler(t, k):
    return np.exp(math.tau * 1j * k * t)


def main():

    fig, ax = plt.subplots(N, 1, sharex=False, constrained_layout=True)
    # fig.tight_layout()
    x = np.linspace(0, 1, num=100)

    fig.suptitle("DFT basis functions")
    for k in range(N):
        ax[k].set_title(f"n = {k}", loc="left")
        y1 = np.real(euler(x, k))
        y2 = np.imag(euler(x, k))

        ax[k].plot(x, y1, label="real part")
        ax[k].plot(x, y2, label="imaginary part")
        ax[k].set_ylim(-1.3, 1.3)
        ax[k].set_xticks([0, 1])
        if k > 1:
            ax[k].set_xticks([0, 1/k, 1], ["0", f"1/{k}", "1"])

    plt.legend(loc="right")
    plt.show()


if __name__ == "__main__":
    main()
