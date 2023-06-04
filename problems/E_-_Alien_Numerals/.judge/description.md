# E. Alien Numerals

After landing on planet D, you find out that the aliens there use the same symbols for digits in their decimal number system as we do, but they assign different values to them. In particular, they assign the value $p_i$ to the digit $i$ of our decimal system. For example, if $p_1 = 3$, then the aliens assign the value $3$ to the digit $1$ of our decimal system.

You are given two integers $a$ and $b$ consisting of decimal digits. Write a program to compare the values of $a$ and $b$ in the aliens' decimal number system.

## Input

The first line of input contains 10 integers $p_0, p_1, \dots, p_9$ ($0 \leq p_i \leq 9$). $p_i$ is the value the aliens assign to the digit symbol $i$ of our decimal system. For example, if $p_1 = 3$, then the aliens assign the value $3$ to the digit $1$ of our decimal system. No two $p_i$'s are equal.

The second line of input contains in integer $n$ ($1 \leq n \leq 100$), the number of digits in the integers $a$ and $b$.

The second line of input contains the integer $a$ consisting of $n$ digits.

The third line of input contains the integer $b$ consisting of $n$ digits.

## Output

Print the symbol

* `<` if the value of $a$ is less than the value of $b$ in the aliens' decimal system;
* `>` if the value of $a$ is greater than the value of $b$ in the aliens' decimal system;
* `=` if the value of $a$ is equal to the value of $b$ in the aliens' decimal system.

## Samples

### Sample #1

+-----------------------------------------+-----------------------------------------+
| Input                                   | Output                                  |
+=========================================+=========================================+
| ```txt                                  | ```txt                                  |
| 0 1 2 3 4 5 6 7 8 9                     | <                                       |
| 3                                       | ```                                     |
| 101                                     |                                         |
| 102                                     |                                         |
| ```                                     |                                         |
+-----------------------------------------+-----------------------------------------+

### Sample #2

+-----------------------------------------+-----------------------------------------+
| Input                                   | Output                                  |
+=========================================+=========================================+
| ```txt                                  | ```txt                                  |
| 0 1 2 3 4 5 6 7 8 9                     | =                                       |   
| 3                                       | ```                                     |
| 101                                     |                                         |
| 101                                     |                                         |
| ```                                     |                                         |
+-----------------------------------------+-----------------------------------------+

### Sample #3

+-----------------------------------------+-----------------------------------------+
| Input                                   | Output                                  |
+=========================================+=========================================+
| ```txt                                  | ```txt                                  |
| 1 5 0 2 9 8 6 3 7 4                     | <                                       |
| 3                                       | ```                                     |
| 020                                     |                                         |
| 027                                     |                                         |
| ```                                     |                                         |
+-----------------------------------------+-----------------------------------------+

### Sample #4

+-----------------------------------------+-----------------------------------------+
| Input                                   | Output                                  |
+=========================================+=========================================+
| ```txt                                  | ```txt                                  |
| 1 5 0 2 9 8 6 3 7 4                     | >                                       |
| 3                                       | ```                                     |
| 025                                     |                                         |
| 027                                     |                                         |
| ```                                     |                                         |
+-----------------------------------------+-----------------------------------------+

## Note

* In the first sample, the value of each digit is the same as its value in our decimal system. So, the value of the number $101$ is $(1 \cdot 10^2 + 0 \cdot 10^1 + 1 \cdot 10^0) = (100 + 0 + 1) = 101$, and the value of the number $102$ is $1 \cdot 10^2 + 0 \cdot 10^1 + 2 \cdot 10^0 = 100 + 0 + 2 = 102$. Since $101 < 102$, the answer is `<`.

* In the fourth sample, the value of the digits $0$, $2$, $5$ and $7$ are $1$, $0$, $8$ and $3$, respectively. So, the value of the number $025$ is $(1 \cdot 10^2 + 0 \cdot 10^1 + 8 \cdot 10^0) = (100 + 0 + 8) = 108$, and the value of the number $027$ is $1 \cdot 10^2 + 0 \cdot 10^1 + 3 \cdot 10^0 = 100 + 0 + 3 = 103$. Since $108 > 103$, the answer is `>`.
