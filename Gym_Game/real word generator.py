from random import *
from string import *

words = ["apple", "banana", "cherry", "date", "elderberry"]

def generate_word(length):
    if length < 1 or length > 10:
        raise ValueError("Length must be between 1 and 10")
    
    word = ''
    for i in range(length):
        word += choice(ascii_lowercase)
    
    return word
def generate_real_word():
    if not words:
        raise ValueError("No words available to choose from")
    
    return choice(words)

if __name__ == "__main__":
    try:
        print("Randomly generated word of length 5:", generate_word(5))
        print("Randomly selected real word:", generate_real_word())
    except ValueError as e:
        print("Error:", e)