import re
pattern = r"^[a-zA-Z0-9]+(?:[._-][a-zA-Z0-9]+)*@[a-zA-Z]+\.[a-zA-Z]{2,}$"
word = "eshwarrsa@gmail.com"
print(re.match(pattern, word))