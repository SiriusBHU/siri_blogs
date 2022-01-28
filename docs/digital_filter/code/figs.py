import numpy as np
import matplotlib.pyplot as plt


t = np.arange(0, 100, 0.1)
f = np.arange(0, 10, 0.01)
x1_t = 3 * np.cos(0.2 * np.pi * t - 0.7 * np.pi)
x2_t = 1 * np.cos(0.5 * np.pi * t + 0.5 * np.pi)
x3_t = 1.5 * np.cos(2 * np.pi * t)

x_t = x1_t + x2_t + x3_t
x_f = np.fft.fft(x_t) / len(f) * 2
a_f = np.abs(x_f)
# p_f = np.angle(x_f)
p_f = np.arctan(x_f.imag / x_f.real) / np.pi * 180

plt.figure()
plt.subplot(311)
plt.plot(t, x1_t)
plt.xlim(0, 100)
plt.ylim(-6, 6)
plt.subplot(312)
plt.plot(t, x2_t)
plt.xlim(0, 100)
plt.ylim(-6, 6)
plt.subplot(313)
plt.plot(t, x3_t)
plt.xlim(0, 100)
plt.ylim(-6, 6)

plt.figure()
plt.plot(t, x_t)
plt.xlim(0, 100)
plt.ylim(-6, 6)

plt.figure()
plt.subplot(211)
plt.plot(f, a_f)
# plt.xticks(np.arange(0, 5, 0.1))
plt.yticks(np.arange(0, 3, 0.5))
plt.xlim(0, 5)
plt.grid(True)
plt.scatter(f[10], a_f[10], c="r", s=20)
plt.scatter(f[25], a_f[25], c="r", s=20)
plt.scatter(f[100], a_f[100], c="r", s=20)
plt.text(f[10], a_f[10], (f[10], np.round(a_f[10], 2)), c='r')
plt.text(f[25], a_f[25], (f[25], np.round(a_f[25], 2)), c='r')
plt.text(f[100], a_f[100], (f[100], np.round(a_f[100], 2)), c='r')

plt.subplot(212)
plt.plot(f, p_f, lw=0.7)
plt.xlim(0, 5)
plt.grid(True)
plt.scatter(f[10], p_f[10], c="r", s=20)
plt.scatter(f[25], p_f[25], c="r", s=20)
plt.scatter(f[100], p_f[100], c="r", s=20)
plt.text(f[10], p_f[10], (f[10], np.round(p_f[10], 2)), c='r')
plt.text(f[25], p_f[25], (f[25], np.round(p_f[25], 2)), c='r')
plt.text(f[100], p_f[100], (f[100], np.round(p_f[100], 2)), c='r')


plt.show()




