import random
from The_sets import episode_1b
from The_sets import episode_1a, episode_1c





a = 10
while a!=0:
    x=random.randint(0,5)
    print('Choose from the list: ')
    for number,episode in enumerate(episode_1a):
        print(number +1,episode)
    print('Press 0 to exit')

    a = input('-')
    a=int(a)
    if a ==0:
        break
    else:
        print(episode_1a[a-1] + episode_1b[x])
        print()
        print('*' * 12)

print('Thanks for playing!')