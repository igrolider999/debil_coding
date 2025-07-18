import time
import sys

text = "Hello world"

# Печатаем первые 4 буквы по одной с паузой
for i in range(6):  # H e l l
    print(text[i], end='', flush=True)
    time.sleep(0.5)

# Удаляем 2 буквы (две "l")
for _ in range(2):
    print('\b \b', end='', flush=True)  # \b - возврат назад, ' ' - замена на пробел
    time.sleep(0.5)

# Печатаем заново последние буквы "llo world" начиная с индекса 2
for i in range(2, len(text)):
    print(text[i], end='', flush=True)
    time.sleep(0.5)

print()  # перевод строки в конце