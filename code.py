import random

firstline = ['maska opadła', 'maska wraca', 'maska skruszała']
secondline = ['zagubione ciało', 'zagubione serce', 'zagubiony umysł']
thirdline = ['milknie i zanika', 'krzyczy w ciszy', 'cieszy się bólem']

a = int(random.uniform(0, 3))
b = int(random.uniform(0, 3))
c = int(random.uniform(0, 3))

print(firstline[a])
print(secondline[b])
print(thirdline[c])