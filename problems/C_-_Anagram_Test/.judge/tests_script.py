import random


def random_length(test_idx):
    lengths = [5, 10, 20, 100, 1000, 100000]
    length_idx = min(test_idx, 5)
    is_random_length = random.choice([True, False])
    return (
        lengths[length_idx]
        if not is_random_length else
        random.randint(1, lengths[length_idx])
    )


tests = [
    'anagram\nnagaram',
    'binary\nbrainy',
    'qwerty\nqwerrty',
]

for test_idx in range(len(tests), 100):
    s = ''
    t = ''

    make_anagram = random.choice([True, False])
    if make_anagram:
        length = random_length(test_idx)
        s = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz')
                    for _ in range(length))
        chars_in_s = list(s)
        random.shuffle(chars_in_s)
        t = ''.join(chars_in_s)
    else:
        length_s = random_length(test_idx)
        length_t = random_length(test_idx)            
        s = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz')
                    for _ in range(length_s))
        t = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz')
                    for _ in range(length_t))

    test = f'{s}\n{t}\n'
    tests.append(test)
