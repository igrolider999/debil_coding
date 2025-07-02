from random import *
from string import *

words = ["apple", "banana", "cherry", "date", "elderberry"]

def generate_word(length):
    global word
    if length < 1 or length > 10:
        raise ValueError("Length must be between 1 and 10")
    
    word = choice(words)
    for i in range(length):
        word += choice(ascii_lowercase)

generate_word(9)
print(word)