import matplotlib.pyplot as plt

def load_values(path):
    with open(path) as f:
        return [float(line) for line in f if line.strip()]

def plot_series(
    ax, y, highlight,
    *,
    linestyle=":",
    color="black",
    linewidth=1.2,
    circle_size=4,
    x_size=4
):
    x = list(range(1, len(y) + 1))
    h = set(highlight)   # 0-based indices

    # connecting line (LOW zorder)
    ax.plot(
        x, y,
        linestyle=linestyle,
        color=color,
        linewidth=linewidth,
        zorder=1
    )

    # non-highlight points → open circles (HIGH zorder)
    for i in range(len(y)):
        if i in h:
            continue
        ax.plot(
            x[i], y[i],
            marker="o",
            color=color,
            markersize=circle_size,
            markerfacecolor="white",
            markeredgewidth=1.2,
            linestyle="None",
            zorder=3
        )

    # highlighted points → x marker (HIGHEST zorder)
    for i in h:
        if 0 <= i < len(y):
            ax.plot(
                x[i], y[i],
                marker="x",
                color=color,
                markersize=x_size,
                linestyle="None",
                zorder=4
            )

# -------------------------
# load datasets
# -------------------------
y1 = load_values("translace.dat")
y2 = load_values("rotace.dat")

# separate highlights (0-based)
highlight1 = [0, 7, 14]
highlight2 = [0, 5, 7, 10, 14]

# -------------------------
# plot
# -------------------------
plt.rcParams["svg.fonttype"] = "none"

plt.figure(figsize=(3, 1.5))
ax = plt.gca()

# dataset 1 → dotted, black
plot_series(
    ax,
    y1,
    highlight1,
    linestyle=":",
    color="black"
)

# dataset 2 → dashed, orange
plot_series(
    ax,
    y2,
    highlight2,
    linestyle="--",
    color="orange"
)

# half-open frame
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_linewidth(1.2)
ax.spines["bottom"].set_linewidth(1.2)

# no ticks / labels
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel("")
ax.set_ylabel("")

plt.tight_layout()
plt.savefig("figS14_plot.svg")
plt.show()
