# Funktion zur Zählung eines bestimmten Wortes in einer Textdatei
def count_word_in_file(filename, word_to_count):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        word_count = text.lower().count(word_to_count.lower())
        return word_count
    except FileNotFoundError:
        print(f"Datei '{filename}' nicht gefunden.")
        return 0

# Vollständiger Pfad zur Datei
filename = r'C:\Users\Elisa\Desktop\Py_Training\bibel.txt'
word_to_count = 'Gott'
count = count_word_in_file(filename, word_to_count)

print(f"Das Wort '{word_to_count}' kommt {count} Mal in der Datei '{filename}' vor.")