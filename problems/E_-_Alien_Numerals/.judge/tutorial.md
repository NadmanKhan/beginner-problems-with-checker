# Tutorial for Problem E - Alien Numerals

Remember that the place-value of a digit is determined by its position in the number. For example, in the number $123$, the place-value of $1$ is $100$, the place-value of $2$ is $10$, and the place-value of $3$ is $1$. The value of the number is the sum of the digits multiplied by their corresponding place-values, i.e. $123 = 1 \cdot 100 + 2 \cdot 10 + 3 \cdot 1 = 100 + 20 + 3$. The number system in the problem works the same way, except the meaning (or value) of a digit may be different (e.g., the value of $1$ may be $5$ instead of $1$).

An important observation is that input numbers cannot be taken as integers, since they may be too large to fit in an integer. Instead, we can read the input as strings.

### Main Idea

For any two integers having the same "length" (number of digits), the "lexicographically" greater integer is also the one with the greater value. In other words, if we keep comparing the two integers from most-signifcant (left-most) digit to least-significant (right-most) digit, the first time we encounter a digit that is greater in one integer than the other, we can assert that the integer with the greater digit has the greater value. If we reach the end of both integers without finding an unequal digit, then the two integers have the same value.

### Code

```c
#include <stdio.h>

int main() {
    
    int value[10];
    for (int i = 0; i < 10; i++) {
        scanf("%d", &value[i]);
    }

    int n;
    scanf("%d", &n);

    char a[100 + 10];
    scanf("%s", a);

    char b[100 + 10];
    scanf("%s", b);

    for (int i = 0; i < n; ++i) {
        int digit_a = a[i] - '0';
        int digit_b = b[i] - '0';
        int value_a = value[digit_a];
        int value_b = value[digit_b];
        if (value_a > value_b) {
            printf(">\n");
            return 0;
        } else if (value_a < value_b) {
            printf("<\n");
            return 0;
        }
    }

    printf("=\n");

    return 0;
}
```