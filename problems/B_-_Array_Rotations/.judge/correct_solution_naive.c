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

    // rotate k times
    while (k--) {
        // copy last element to temp[0]
        temp[0] = a[n - 1];
        // copy all elements from a[0 .. n - 2] to temp[1 .. n - 1]
        for (int i = 0; i < n - 1; ++i) {
            temp[i + 1] = a[i];
        }
        // copy all elements from temp back to a
        for (int i = 0; i < n; ++i) {
            a[i] = temp[i];
        }
    }

    for (int i = 0; i < n; ++i) {
        printf("%d ", a[i]);
    }

    printf("\n");

    return 0;
}