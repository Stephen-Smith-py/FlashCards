import itertools
import random

cards = {"List copy": "O(n)", "Append[1]": "O(1)", "Pop last": "O(1)", "Pop intermediate": "O(n)", "Insert": "O(n)",
         "Get item": "O(1)", "Set item": "O(1)", "Delete item": "O(n)", "Iteration": "O(n)", "Get slice": "O(k)",
         "Delete slice": "O(n)", "Set slice": "O(k + n)", "Extend[1]": "O(k)", "Sort": "O(n log n)",
         "Multiply": "O(nk)", "x in s": "O(n)", "min/max": "O(n)", "Length": "O(1)"}

keys = list(cards.keys())
random.shuffle(keys)

for key in keys:
    print(key)
    if input() != cards.get(key):
        print(cards.get(key) + "\n")
