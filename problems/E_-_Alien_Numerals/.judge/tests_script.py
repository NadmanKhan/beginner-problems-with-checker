import random

tests = [
    '0 1 2 3 4 5 6 7 8 9\n'
    '3\n'
    '101\n'
    '102',

    '0 1 2 3 4 5 6 7 8 9\n'
    '3\n'
    '101\n'
    '101',

    '1 5 0 2 9 8 6 3 7 4\n'
    '3\n'
    '020\n'
    '027',

    '1 5 0 2 9 8 6 3 7 4\n'
    '3\n'
    '025\n'
    '027',
]

for test_idx in range(len(tests), 100):
    digits = list(map(str, range(10)))
    random.shuffle(digits)

    n = random.randint(1, 100)
    a = list(random.choice(digits) for _ in range(n))
    b = list(x for x in a)


    change = random.choice([True, True, False])
    if change:
        for i in range(n):
                change_this = random.choice([True, False, False])
                if change_this:
                    b[i] = random.choice(digits)

    test = (
        ' '.join(digits) + '\n'
        + f'{n}\n'
        + ''.join(a) + '\n'
        + ''.join(b) + '\n'
    )

    tests.append(test)
