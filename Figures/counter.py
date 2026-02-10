import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# -------------------------------------------------------
# Counterexample coordinates from your solver output
# -------------------------------------------------------

u = (0.0, 0.0)

# five two-demand points (x_i)
x_points = [
    (-0.65, -0.30),
    (-0.65, -0.65),
    (-0.30, -0.30),
    (-0.30, -0.65),
    (0.05, -0.65),
]

# corresponding second supplies (w_i)
w_points = [
    (-0.8005551430754256, -0.3726040426072678),
    (-0.9365441122658427, -1.1912535425044153),
    (-0.6019427617211679, -1.132035344465582),
    (-0.8383023516633807, -1.2781683809950704),
    (0.28207303944448625, -1.2022113216687005),
]


# -------------------------------------------------------
# Plot Setup
# -------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect("equal")

# Axis limits
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)

# -------------------------------------------------------
# Draw central supplier u
# -------------------------------------------------------
ax.add_patch(Circle(u, 0.07, color="blue", zorder=5))
ax.text(u[0] + 0.05, u[1] + 0.05, "u", fontsize=12)

# dashed radius-1 circle around u
ax.add_patch(
    Circle(u, 1.0, edgecolor="blue", linestyle="--", fill=False, alpha=0.7, lw=1.3)
)

# -------------------------------------------------------
# Draw two-demand points x_i
# -------------------------------------------------------
for i, xi in enumerate(x_points):
    ax.add_patch(Circle(xi, 0.06, facecolor="green", edgecolor="black", zorder=5))
    ax.text(xi[0] + 0.06, xi[1] + 0.06, f"$x_{i+1}$", fontsize=12)
    ax.plot([u[0], xi[0]], [u[1], xi[1]], color="gray", linewidth=1.1)


# -------------------------------------------------------
# Draw second supplies w_i + their unit disks
# -------------------------------------------------------
for i, wi in enumerate(w_points):
    ax.add_patch(Circle(wi, 0.06, facecolor="red", edgecolor="black", zorder=5))
    ax.text(wi[0] + 0.06, wi[1] + 0.06, f"$w_{i+1}$", fontsize=12)

    # link xi → wi
    xi = x_points[i]
    ax.plot([xi[0], wi[0]], [xi[1], wi[1]], color="gray", linewidth=1.0)

    # light orange disk radius 1 around each w_i
    ax.add_patch(
        Circle(
            wi,
            1.0,
            facecolor="orange",
            alpha=0.12,
            edgecolor="none",
            zorder=1,
        )
    )

# -------------------------------------------------------
# Legend-like text
# -------------------------------------------------------
ax.text(1.1, 1.9, r"$u \in V_2$", color="blue", fontsize=12)
ax.text(1.1, 1.7, r"$x_i \in V_0(2)$", color="green", fontsize=12)
ax.text(1.1, 1.5, r"$w_i \in V_2$", color="red", fontsize=12)

# Title
ax.set_title(
    "Counterexample: 5 two-demand vertices served by a single $V_2$ vertex",
    fontsize=14,
)

# Save outputs
plt.tight_layout()
plt.savefig("counterexample_drdf.png", dpi=350)
plt.savefig("counterexample_drdf.pdf")
plt.show()
