from collections import Counter
import re

def count_unique_words(text):
    cleaned_text = re.sub(r'[^\w\s]', '', text).lower()
    words = cleaned_text.split()
    word_counts = Counter(words)
    return len(word_counts)

text = "veni ??? vidi, vici!"
unique_word_count = count_unique_words(text)
print(f"Количество уникальных слов: {unique_word_count}")