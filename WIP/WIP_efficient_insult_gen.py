# NOTE: This is a work in progress, I've been trying to figure out how to make the insult generator more efficient.
# Current version (WIP)
from random import choice
adjectives = ["wet", "big"]
nouns = ["turnip", "dog"]
insult = choice(adjectives + nouns)
print("You are a ", insult)

# Original version
# from random import choice
# adjectives = ["wet", "big"]
# nouns = ["turnip", "dog"]
# print("You are a ")
# adjective = choice(adjectives)
# print(adjective)
# print(choice(nouns))
