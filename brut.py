import itertools

letters = 'abcdefghijklmnopqrstuvwxyz'

for i in range(1, 6):
     combinations = itertools.product(letters, repeat=i)
     for combination in combinations:
             print(''.join(combination))