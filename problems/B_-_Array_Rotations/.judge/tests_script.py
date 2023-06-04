import random

tests = [
    '5 1\n'
    '1 2 3 4 5',

    '5 2\n'
    '1 2 3 4 5',


    '5 5\n'
    '1 2 3 4 5',
]

for test_idx in range(len(tests), 100):
    n = random.randint(1, 100)
    k = random.randint(1, 100)
    a = [random.randint(1, 100) for _ in range(n)]
    
    test = f'{n} {k}\n' + ' '.join(map(str, a))

    tests.append(test)
