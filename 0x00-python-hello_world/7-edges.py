#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3]  # Extract the first 3 letters
word_last_2 = word[-2:]  # Extract the last 2 letters
middle_start = (len(word) - 2) // 2
middle_end = middle_start + 2
middle_word = word[middle_start:middle_end]  # Extract the middle word
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
