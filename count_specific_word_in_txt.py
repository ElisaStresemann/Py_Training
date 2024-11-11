# Funktion zur Zählung mehrerer Wörter in einer Textdatei
def count_words_in_file(filename, words_to_count):
    word_counts = {word: 0 for word in words_to_count}  # Wörter initialisieren

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read().lower()  # Text in Kleinbuchstaben umwandeln, um Groß-/Kleinschreibung zu ignorieren

        # Jedes Wort zählen
        for word in words_to_count:
            word_counts[word] = text.count(word.lower())

        return word_counts
    except FileNotFoundError:
        print(f"Datei '{filename}' nicht gefunden.")
        return None

# Vollständiger Pfad zur Datei
filename = r'C:\Users\Elisa\Documents\GitHub\Py_Training\bibel.txt'
words_to_count = ['Gott', 'zum', 'ist']  # Liste der Wörter, die gezählt werden sollen

# Aufruf der Funktion
counts = count_words_in_file(filename, words_to_count)

# Ausgabe der Ergebnisse
if counts is not None:
    for word, count in counts.items():
        print(f"Das Wort '{word}' kommt {count} Mal in der Datei '{filename}' vor.")
