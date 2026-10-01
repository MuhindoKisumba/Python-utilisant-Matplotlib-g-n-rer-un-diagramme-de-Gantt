import matplotlib.pyplot as plt
import pandas as pd

# Données du projet
data = {
    "Tâche": ["Analyse", "Conception", "Développement", "Tests", "Déploiement"],
    "Début": ["2026-06-01", "2026-06-04", "2026-06-06", "2026-06-11", "2026-06-14"],
    "Fin": ["2026-06-03", "2026-06-05", "2026-06-10", "2026-06-13", "2026-06-15"]
}

df = pd.DataFrame(data)

df["Début"] = pd.to_datetime(df["Début"])
df["Fin"] = pd.to_datetime(df["Fin"])
df["Durée"] = (df["Fin"] - df["Début"]).dt.days

fig, ax = plt.subplots(figsize=(10, 5))

for i, row in df.iterrows():
    ax.barh(
        row["Tâche"],
        row["Durée"],
        left=row["Début"].toordinal(),
        height=0.5
    )

# Formatage de l'axe des dates
dates = pd.date_range(df["Début"].min(), df["Fin"].max())
ax.set_xticks([d.toordinal() for d in dates])
ax.set_xticklabels([d.strftime("%d/%m") for d in dates], rotation=45)

ax.set_title("Diagramme de Gantt du projet")
ax.set_xlabel("Date")
ax.set_ylabel("Tâches")

plt.tight_layout()
plt.show()