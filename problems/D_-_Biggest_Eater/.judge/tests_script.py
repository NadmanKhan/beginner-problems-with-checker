import random

tests = [
    '3\n'
    '2 1 2\n'
    '3 3 1 2\n'
    '2 4 3',

    '2\n'
    '2 1 2\n'
    '2 1 2',

    '1\n'
    '1 1',

    '5\n' +
    '\n'.join(
        (' '.join('5' for _ in range(5 + 1))) for _ in range(5)
    ),

    '100\n' +
    '\n'.join(
        (' '.join('100' for _ in range(100 + 1))) for _ in range(100)
    )
]

for test_idx in range(len(tests), 100):
    n = random.randint(1, 100)
    test = f'{n}\n'
    for _ in range(n):
        m = random.randint(1, 100)
        test += (
            f'{m} ' +
            ' '.join(str(random.randint(1, 100)) for _ in range(m)) + '\n'
        )
    
    tests.append(test)
