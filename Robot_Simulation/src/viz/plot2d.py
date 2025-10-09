import matplotlib.pyplot as plt
import numpy as np
import math

def plot_path_with_heading(xs, ys, yaws=None, ideal_square_side=None, save_path=None):
    plt.figure(figsize=(5,5)); plt.axis("equal"); plt.grid(True, ls="--", alpha=0.5)
    plt.plot(xs, ys, linewidth=2, label="path")
    if ideal_square_side is not None:
        s = ideal_square_side
        square = np.array([[0,0],[s,0],[s,s],[0,s],[0,0]])
        plt.plot(square[:,0], square[:,1], "k--", label="ideal square")
    if yaws is not None and len(xs):
        # 마지막 헤딩 화살표
        L = 0.15
        hx = L*math.cos(yaws[-1]); hy = L*math.sin(yaws[-1])
        plt.arrow(xs[-1], ys[-1], hx, hy, head_width=0.05, head_length=0.08, color="r")
    plt.legend()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches="tight")
    else:
        plt.show()
