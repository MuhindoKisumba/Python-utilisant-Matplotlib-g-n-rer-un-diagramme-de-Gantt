import matplotlib.pyplot as plt

# Tâches : (Nom, début, durée)
tasks = [
    ("Analyse", 0, 3),
    ("Conception", 3, 2),
    ("Développement", 5, 5),
    ("Tests", 10, 3),
    ("Déploiement", 13, 2)
]

fig, ax = plt.subplots(figsize=(10, 5))

for i, (task, start, duration) in enumerate(tasks):
    ax.barh(task, duration, left=start, height=0.5)

ax.set_xlabel("Temps (jours)")
ax.set_ylabel("Tâches")
ax.set_title("Diagramme de Gantt")
ax.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()