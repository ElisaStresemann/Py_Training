import matplotlib.pyplot as plt

# Kanisterzustände (8L, 5L, 3L)
states = [
    (8, 0, 0),  # Start
    (3, 5, 0),  # Schritt 1
    (3, 2, 3),  # Schritt 2
    (6, 2, 0),  # Schritt 3
    (6, 0, 2),  # Schritt 4
    (1, 5, 2),  # Schritt 5
    (1, 4, 3)   # Schritt 6 (Ergebnis)
]

# Farben für die Kanister
colors = ['pink', 'purple', 'orange']

# Erstellen der Grafik
fig, ax = plt.subplots(figsize=(10, 6))
x_labels = [f"Schritt {i}" for i in range(len(states))]

# Zeichne die Zustände für jeden Kanister
for i, color in enumerate(colors):
    values = [state[i] for state in states]
    ax.bar([x + i * 0.25 for x in range(len(states))], values, width=0.25, label=f'{8 - 3 * i}-Liter-Kanister', color=color)

# Achsenbeschriftung und Titel
ax.set_xlabel('Schritte')
ax.set_ylabel('Liter')
ax.set_title('Schritte zur Lösung des Kanisterproblems')
ax.set_xticks([x + 0.25 for x in range(len(states))])
ax.set_xticklabels(x_labels, rotation=45)
ax.legend()

# Grafik anzeigen
plt.tight_layout()
plt.show()
