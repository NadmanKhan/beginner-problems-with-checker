import random

tests = [
    '4\n'
    '8',

    '-2147483648\n'
    '2147483647'
    
    '1000000000000000000\n'
    '1000000000000000000',
]

for test_idx in range(len(tests), 100):
    exponent = [1, 3, 9, 18][test_idx // 25]
    upper_bound = 10 ** exponent
    lower_bound = -upper_bound
    a = random.randint(lower_bound, upper_bound)
    b = random.randint(lower_bound, upper_bound)
    test = f'{a}\n{b}'

    tests.append(test)
