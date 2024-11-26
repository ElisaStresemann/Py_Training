"""AUFGABE:
Sie haben ein Array von Objekten (Musikalben). 
Extrahieren sie alle Songtitel der Alben und speichern sie in einem neuen Array.
Jeder Titel darf nur einmal vorkommen. """


# Beispiel-Array von Musikalben - hier dict, das 2 Werte je Album
# Jedes Album ist ein Wörterbuch (dict) mit zwei Einträgen: dem Albumnamen ("name") und einer Liste von Titeln ("titel").
alben = [
    {"name": "Album 1", "titel": ["Song A", "Song B", "Song C"]},  # Wörterbuch mit Albumname und Liste von Songtiteln
    {"name": "Album 2", "titel": ["Song B", "Song D", "Song E"]},
    {"name": "Album 3", "titel": ["Song F", "Song C", "Song G"]}
]

# Set für eindeutige Title erstellem
# Set enthält nur eindeutige Werte
eindeutige_werte = set()

# Alle Song"titel" extrahieren
for album in alben:                             # Schleife über jedes Album im 'alben'-Array
    eindeutige_werte.update(album["titel"])     # Titel jedes Albums zum Set hinzufügen. Duplikate werden automatisch entfernt.

#eindeutige_titel_liste = sorted(list(eindeutige_titel))  # In Liste umwandeln und sortieren -> Gibt eine neue, sortierte Liste zurück. Die ursprüngliche Liste bleibt unverändert.

eindeutige_titel_liste = list(eindeutige_werte) # Set in Liste umwandeln 
eindeutige_titel_liste.sort()                   # Sortiert und verändert die originale Liste.
print(eindeutige_titel_liste)
