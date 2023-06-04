# Tutorial for Problem D - Biggest Eater

The problem statement is pretty straightforward. We just need to find the person who eats the most.

We can do this by keeping track of the index of the person who eats the most (let's call it `ans_idx`) and the sum of the food eaten by that person (let's call it `ans_sum`). For each person, we read the number of food items eaten by that person and add it a local running sum (let's call it `tmp_sum`, indicating "temporary sum"). If `tmp_sum` is greater than `ans_sum`, we update the index and the sum.

### Code

```c
#include <stdio.h>

int main() {

    int ans_idx = 0;
    int ans_sum = 0;

    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        int m;
        scanf("%d ", &m);
        int tmp_sum = 0;
        while (m--) {
            int x;
            scanf("%d", &x);
            tmp_sum += x;
        }
        
        if (tmp_sum > ans_sum) {
            ans_sum = tmp_sum;
            ans_idx = i + 1;
        }
    }

    printf("%d\n", ans_idx);

    return 0;
}
```