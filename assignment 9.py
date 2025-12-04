

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
text = "Natural Language Processing helps computers understand human language."
tokens = word_tokenize(text)
stop_words = set(stopwords.words('english'))
filtered = [word for word in tokens if word.lower() not in stop_words]

print("Original Text:")
print(text)

print("\nTokenized Words:")
print(tokens)

print("\nAfter Removing Stopwords:")
print(filtered)
