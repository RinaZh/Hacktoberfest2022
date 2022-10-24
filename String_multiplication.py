import random
word = input("Say something to see how many times it echoes: ")
word += " "

echo = random.randint(2, 8)
print(word * echo)