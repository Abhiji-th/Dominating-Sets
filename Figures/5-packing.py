# plot_drdf_maximally_apart.py
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

fig, ax = plt.subplots(figsize=(6,6))
ax.set_aspect('equal')

# ---------------------------------------------------------------
# 1. Central vertex u
# ---------------------------------------------------------------
u = np.array([0.0, 0.0])
ax.add_patch(Circle(u, 1.0, edgecolor='blue', facecolor='none',
                    lw=1.5, ls='--'))

# ---------------------------------------------------------------
# 2. Five maximally apart demand-vertices inside the disk
# ---------------------------------------------------------------
r = 0.95              # close to boundary but inside
angles = np.linspace(90, 450, 6)[:-1] * np.pi/180
x = [np.array([r*np.cos(a), r*np.sin(a)]) for a in angles]

for i, xi in enumerate(x, start=1):
    ax.add_patch(Circle(xi, 0.05, facecolor='lime', edgecolor='black'))
    ax.text(xi[0]+0.05, xi[1]+0.05, f"$x_{i}$", fontsize=12)
    ax.plot([u[0], xi[0]], [u[1], xi[1]], 'gray', lw=0.7)

# ---------------------------------------------------------------
# 3. Second suppliers forced into lens intersection regions
# ---------------------------------------------------------------
w = []
for xi in x:
    direction = xi / np.linalg.norm(xi)
    # Move slightly outward then pull back inside central disk
    wi = xi + 0.40 * direction   # inside B(xi,1)
    wi = wi * 0.84               # compress to be inside B(u,1)
    w.append(wi)

for i, wi in enumerate(w, start=1):
    ax.add_patch(Circle(tuple(wi), 0.05, facecolor='red', edgecolor='black'))
    ax.text(wi[0]+0.05, wi[1]+0.05, f"$w_{i}$", fontsize=12)
    ax.plot([x[i-1][0], wi[0]], [x[i-1][1], wi[1]], 'gray', lw=0.7)

# ---------------------------------------------------------------
# 4. Show supplier unit disks to illustrate heavy overlap
# ---------------------------------------------------------------
for wi in w:
    ax.add_patch(Circle(tuple(wi), 1.0, facecolor='orange', alpha=0.12))

ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.set_title("Maximally apart five 2-demand vertices inside a UDG\n→ Forced second suppliers conflict")
plt.tight_layout()
plt.savefig("maximally_apart_5.png", dpi=300)
plt.show()
