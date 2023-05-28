import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np

import trip_modificators as tmode
from stops import Stop, KeyStop

YMIN, YMAX, STEP = -20, 20, 2

def generate_graph_base(route):
    fig, ax = plt.subplots(1, 1, figsize=(14, 14), dpi=80)
    dists = []
    for s in route:
        color = "gray"
        linewidth = 1
        if isinstance(s, KeyStop):
            color = "black"
            linewidth = 2
        ax.vlines(x=s.dist, ymin=YMIN - 1, ymax=YMAX + 1, color=color, alpha=0.8, linewidth=linewidth, linestyles="dotted")
        dists.append(s.dist)

    for i in range(-STEP, YMIN - 1, -STEP):
        ax.hlines(y=i, xmin=0, xmax = dists[-1], color = "gray", alpha = 0.5, linewidth=1, linestyles="dotted")
        
    for i in range(STEP, YMAX + 1, STEP):
        ax.hlines(y=i, xmin=0, xmax = dists[-1], color = "gray", alpha = 0.5, linewidth=1, linestyles="dotted")


    ax.hlines(y=0, xmin=0, xmax = dists[-1], color = "gray", alpha = 0.5, linewidth=2, linestyles="dashed")
    ax.set_title(f"Моделирование профиля отставаний рейсов маршрута общественного транспорта {route.name}")

    ax.set_xticks(dists)
    plt.xticks(rotation=-90)
    ax.set_xticklabels(map(str, dists))
    ax.set_yticks(np.arange(YMIN, YMAX + 1, STEP))

    plt.gca().spines["top"].set_alpha(.0)
    plt.gca().spines["bottom"].set_alpha(.0)
    plt.gca().spines["right"].set_alpha(.0)
    plt.gca().spines["left"].set_alpha(.0)

    stats = {}
    for s in route:
        if isinstance(s, KeyStop):
            stats[s.dist] = {"Stop": s, "ignore": [], "classic": [], "improved": []}

    return (fig, ax), stats


def add_trip(fig, ax, route, trip, mode="ignore", stats = {}):

    # def count_stats(stats, route, trip, mode):
    #     for relax, time in zip(map(lambda x: 1 if isinstance(x, KeyStop) else 0, route), trip):
    #         if relax:


    modes = {
        "ignore": {"modify": tmode.no_modify, "color": "grey"},
        "classic": {"modify": tmode.classic_modify, "color": "red"},
        "improved": {"modify": tmode.improved_modify, "color": "blue"},
    }
    new_trip = modes[mode]["modify"](route, trip)
    
    for s, k in zip(route, new_trip):
        if (isinstance(s, KeyStop)):
            stats[s.dist][mode].append(k)

    lateness = list(map(lambda x: (x[1] - x[0].scheduled), zip(route, new_trip)))
    # for s, t, nt, lt in zip(route, trip, new_trip, lateness):
    #     print(s, t, nt, lt)


    line = mlines.Line2D(list(map(lambda x: x.dist, route)), lateness, color=modes[mode]["color"], marker='o', alpha=0.3, markersize=6)
    ax.add_line(line)


def show():
    plt.show()