import numpy as np
import pandas as pd
import scipy
from scipy import signal

import matplotlib.pyplot as plt


def get_coefficients(win_len, order):
    if not isinstance(win_len, int) or win_len <= 0:
        raise AttributeError()

    if not isinstance(order, int) or order < 0:
        raise AttributeError()

    if win_len % 2 != 1:
        raise AttributeError()

    if win_len <= order:
        raise AttributeError()

    a = np.arange(win_len)
    a = a - win_len // 2

    order = np.arange(order + 1).reshape(-1, 1)
    A = a ** order





coe = signal.savgol_coeffs(21, 3)


A = np.arange(21)
