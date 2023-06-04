#include <stdio.h>

#define MAX_SIZE 1'000

int a[MAX_SIZE + 10];
int temp[MAX_SIZE + 10];

int main() {
    
    int n, k;
    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; ++i) {
        scanf("%d", &a[i]);
    }

    k = k % n;

    // copy k elements from the end of a to the beginning of temp
    for (int i = 0; i < k; ++i) {
        temp[i] = a[n - k + i];
    }
    // copy the remaining (n - k) elements to the end of temp
    for (int i = k; i < n; ++i) {
        temp[i] = a[i - k];
    }
    // copy all elements from temp back to a
    for (int i = 0; i < n; ++i) {
        a[i] = temp[i];
    }

    for (int i = 0; i < n; ++i) {
        printf("%d ", a[i]);
    }
    printf("\n");

    return 0;
}