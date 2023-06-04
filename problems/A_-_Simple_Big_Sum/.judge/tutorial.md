# Tutorial for Problem A - Simple Big Sum

There is nothing special about this problem except for the constraints being too big for a 32-bit integer. As is stated in the "Note" section of the problem, you should use a 64-bit integer to store the sum, e.g. `long long` in C/C++. Using `int` will cause overflow and you will get a wrong answer.

### Code

```c
#include <stdio.h>

int main() {

    long long x, y;
    scanf("%lld %lld", &x, &y);
    
    long long ans = x + y;
    printf("%lld\n", ans);

    return 0;
}
```
