# C. Anagram Test

You are given two strings $s$ and $t$. Write a program to check if $t$ is an anagram of $s$.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase using all the original letters exactly once. For example, the word `anagram` can be rearranged into `nagaram`, or the word `binary` into `brainy`.

## Input

Input contains two strings $s$ and $t$ in two separate lines. Each string contains only lowercase English letters, and the length of each string is between $1$ and $10^{5}$ inclusive.

## Output

Print `yes` if $t$ is an anagram of $s$, otherwise print `no`.

## Samples

### Sample #1

+-----------------------------------------+-----------------------------------------+
| Input                                   | Output                                  |
+=========================================+=========================================+
| ```txt                                  | ```txt                                  |
| anagram                                 | yes                                     |
| nagaram                                 |                                         |
|                                         | ```                                     |
| ```                                     |                                         |
|                                         |                                         |
+-----------------------------------------+-----------------------------------------+

### Sample #2

+-----------------------------------------+-----------------------------------------+
| Input                                   | Output                                  |
+=========================================+=========================================+
| ```txt                                  | ```txt                                  |
| binary                                  | yes                                     |
| brainy                                  |                                         |
|                                         | ```                                     |
| ```                                     |                                         |
|                                         |                                         |
+-----------------------------------------+-----------------------------------------+

### Sample #3

+-----------------------------------------+-----------------------------------------+
| Input                                   | Output                                  |
+=========================================+=========================================+
| ```txt                                  | ```txt                                  |
| qwerty                                  | no                                      |
| qwerrty                                 |                                         |
|                                         | ```                                     |
| ```                                     |                                         |
|                                         |                                         |
+-----------------------------------------+-----------------------------------------+
