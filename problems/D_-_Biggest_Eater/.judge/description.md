# D. Biggest Eater

In the annual contest of the biggest eater, the winner is the person who eats the most amount of food in a given time. The amount of food is measured in grams.

You are given the amounts, in grams, of food items eaten by the $n$ contestants in the contest, indexed from $1$ to $n$. The $i$-th contestant eats $m_i$ food items, the $j$-th of which weighs $w_{ij}$ grams.

The winner is the contestant who eats the most amount of food. If there are multiple contestants who eat the most amount of food, then the winner is the one who has the smallest index among them. Find the winner of the contest.

## Input

The first line of input contains one integer $n$ ($1 \leq n \leq 100$), the number of contestants.

The next $n$ lines describe the amounts of food eaten by the contestants. The $i$-th of these lines begins with an integer $m_i$ ($1 \leq m_i \leq 100$), the number of food items eaten by the $i$-th contestant. Then follow $m_i$ integers $w_{i1}, w_{i2}, \dots, w_{im_i}$ ($1 \leq w_{ij} \leq 1000$), the weights of the food items eaten by the $i$-th contestant.

## Output

Print one integer, the index of the winner of the contest (the smallest index among the contestants who eat the most amount of food).

## Samples

### Sample #1

+-----------------------------------------+-----------------------------------------+
| Input                                   | Output                                  |
+=========================================+=========================================+
| ```txt                                  | ```txt                                  |
| 3                                       | 2                                       |
| 2 1 2                                   | ```                                     |
| 3 3 1 2                                 |                                         |
| 2 4 3                                   |                                         |
| ```                                     |                                         |
+-----------------------------------------+-----------------------------------------+

### Sample #2

+-----------------------------------------+-----------------------------------------+
| Input                                   | Output                                  |
+=========================================+=========================================+
| ```txt                                  | ```txt                                  |
| 2                                       | 1                                       |
| 2 1 2                                   | ```                                     |
| 2 1 2                                   |                                         |
| ```                                     |                                         |
+-----------------------------------------+-----------------------------------------+

### Sample #3

+-----------------------------------------+-----------------------------------------+
| Input                                   | Output                                  |
+=========================================+=========================================+
| ```txt                                  | ```txt                                  |
| 1                                       | 1                                       |
| 1 1                                     | ````                                    |
| ```                                     |                                         |
+-----------------------------------------+-----------------------------------------+
