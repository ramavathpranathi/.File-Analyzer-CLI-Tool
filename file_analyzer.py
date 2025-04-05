import sys
import string
from collections import Counter

# List of common stop words to ignore
STOP_WORDS = {"the", "is", "and", "a", "an", "in", "on", "of", "to", "for", "with", "at", "by", "from", "it", "this", "that", "are"}

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

def clean_text(text):
    # Convert to lowercase and remove punctuation
    text = text.lower()
    return text.translate(str.maketrans('', '', string.punctuation))

def count_sentences(text):
    # Count '.', '!' and '?' as sentence endings
    return sum(text.count(char) for char in ['.', '!', '?'])

def get_top_words(words, stop_words):
    filtered_words = [word for word in words if word not in stop_words]
    return Counter(filtered_words).most_common(5)

def analyze(file_path):
    text = read_file(file_path)
    sentence_count = count_sentences(text)
    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    word_count = len(words)
    avg_word_len = sum(len(word) for word in words) / word_count if word_count > 0 else 0
    top_words = get_top_words(words, STOP_WORDS)

    # Print analysis
    print("\n--- File Analysis Report ---")
    print(f"Total number of words: {word_count}")
    print("Top 5 most frequent words (excluding stop words):")
    for word, count in top_words:
        print(f"   {word}: {count} times")
    print(f"Average word length: {avg_word_len:.2f}")
    print(f"Number of sentences: {sentence_count}")

# Entry point of the script
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python file_analyzer.py <file.txt>")
    else:
        analyze(sys.argv[1])
