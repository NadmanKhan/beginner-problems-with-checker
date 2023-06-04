# A. Simple Big Sum

You are given two integers $a$ and $b$. Write a program to calculate their sum.

Sounds too easy? See the constrants below, and then read the [Note](#note) section.

## Input

Input contains two integers $a$ and $b$ ($-10^{18} \le a,b \le 10^{18}$) in two seperate lines.

## Output

Print the sum of $a$ and $b$.

## Samples

### Sample #1

+-----------------------------------------+-----------------------------------------+
| Input                                   | Output                                  |
+=========================================+=========================================+
| ```txt                                  | ```txt                                  |
| 4                                       | 12                                      |
| 8                                       | ```                                     |
| ```                                     |                                         |
+-----------------------------------------+-----------------------------------------+

### Sample #2

+-----------------------------------------+-----------------------------------------+
| Input                                   | Output                                  |
+=========================================+=========================================+
| ```txt                                  | ```txt                                  |
| -2147483648                             | -1                                      |
| 2147483647                              | ```                                     |
| ```                                     |                                         |
+-----------------------------------------+-----------------------------------------+

## Note

The range for 32-bit signed integer (`int` or `long` in C/C++) is $-2,147,483,648$ to $2,147,483,647$. Since the input numbers as well as their sum can exceed that range, you will need to use 64-bit integer (`long long` in C/C++). Remember that for `long long` we use the `%lld` format specifier instead of `%d` or `%ld`.
