import math
from matplotlib import pyplot as plt
import numpy as np

N = 5


def euler(t, k):
    return np.exp(math.tau * 1j * k * t)


def main():

    fig, ax = plt.subplots(N, 1, sharex=True)
    x = np.linspace(0, 1, num=50)

    for k in range(N):
        y1 = np.real(euler(x, k))
        y2 = np.imag(euler(x, k))

        ax[k].plot(x, y1)
        ax[k].plot(x, y2)

    plt.show()


if __name__ == "__main__":
    main()
