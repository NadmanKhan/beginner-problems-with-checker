#include <stdio.h>

int main() {

    int ans_idx = 0;
    int ans_sum = 0;

    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        int m;
        scanf("%d ", &m);
        int sum = 0;
        while (m--) {
            int x;
            scanf("%d", &x);
            sum += x;
        }
        if (sum > ans_sum) {
            ans_sum = sum;
            ans_idx = i + 1;
        }
    }

    printf("%d\n", ans_idx);

    return 0;
}