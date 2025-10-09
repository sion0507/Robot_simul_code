import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import math

def animate_path(xs, ys, yaws=None, ideal_square_side=None, out_path="anim.gif", fps=30):
    xs = np.array(xs); ys = np.array(ys); yaws = np.array(yaws) if yaws is not None else None
    fig, ax = plt.subplots(figsize=(5,5)); ax.set_aspect("equal"); ax.grid(True, ls="--", alpha=0.5)
    if ideal_square_side is not None:
        s = ideal_square_side
        ax.plot([0,s,s,0,0],[0,0,s,s,0], "--", linewidth=1)
    path_line, = ax.plot([], [], linewidth=2)
    robot_marker, = ax.plot([], [], marker=(3, 0, 0), markersize=12)
    ax.set_xlim(min(xs.min(),0)-0.2, max(xs.max(),ideal_square_side or 0)+0.2)
    ax.set_ylim(min(ys.min(),0)-0.2, max(ys.max(),ideal_square_side or 0)+0.2)
    def init():
        path_line.set_data([], []); robot_marker.set_data([], [])
        return path_line, robot_marker
    def update(i):
        path_line.set_data(xs[:i+1], ys[:i+1])
        robot_marker.set_data(xs[i], ys[i])
        if yaws is not None:
            robot_marker.set_marker((3, 0, np.degrees(yaws[i])))
        return path_line, robot_marker
    anim = animation.FuncAnimation(fig, update, init_func=init, frames=len(xs), interval=20, blit=True)
    anim.save(out_path, writer=animation.PillowWriter(fps=fps))
    plt.close(fig)
    return out_path
