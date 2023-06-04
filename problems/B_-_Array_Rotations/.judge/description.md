# B. Array Rotations

You are given an array $a$ consisting of $n$ integers. You are also given an integer $k$. You have to rotate the array $k$ times. In each rotation, the last element of the array becomes the first element of the array, and all other elements are shifted one position to the right. For example, if $a = [1, 2, 3, 4, 5]$, then after one rotation, $a = [5, 1, 2, 3, 4]$, and after two rotations, $a = [4, 5, 1, 2, 3]$.

## Input

The first line of input contains two integers $n$ and $k$ ($1 \leq n \leq 100$, $0 \leq k \leq 100$). The second line of input contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \leq a_i \leq 100$).

## Output

Print $n$ space-separated integers -- the elements of the array $a$ after $k$ rotations.

## Samples

### Sample #1

+-----------------------------------------+-----------------------------------------+
| Input                                   | Output                                  |
+=========================================+=========================================+
| ```txt                                  | ```txt                                  |
| 5 1                                     | 5 1 2 3 4                               |
| 1 2 3 4 5                               | ```                                     |
| ```                                     |                                         |
+-----------------------------------------+-----------------------------------------+

### Sample #2

+-----------------------------------------+-----------------------------------------+
| Input                                   | Output                                  |
+=========================================+=========================================+
| ```txt                                  | ```txt                                  |
| 5 2                                     | 4 5 1 2 3                               |
| 1 2 3 4 5                               | ```                                     |
| ```                                     |                                         |
+-----------------------------------------+-----------------------------------------+

### Sample #3

+-----------------------------------------+-----------------------------------------+
| Input                                   | Output                                  |
+=========================================+=========================================+
| ```txt                                  | ```txt                                  |
| 5 5                                     | 1 2 3 4 5                               |
| 1 2 3 4 5                               | ```                                     |
| ```                                     |                                         |
+-----------------------------------------+-----------------------------------------+
