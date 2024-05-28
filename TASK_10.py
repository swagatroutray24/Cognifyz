#Level 2 Task 5

def word_count(filename):
  with open(filename, 'r') as file:
    words = [word.lower() for word in file.read().split()]
  word_counts = {word: words.count(word) for word in set(words)}
  return dict(sorted(word_counts.items()))

filename = input("Enter file name: ")
word_counts = word_count(filename)
for word, count in word_counts.items():
  print(f"{word}: {count}")
