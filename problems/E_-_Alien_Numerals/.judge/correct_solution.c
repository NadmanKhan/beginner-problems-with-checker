#include <stdio.h>

int main() {
    
    int value[10];
    for (int i = 0; i < 10; i++) {
        scanf("%d", &value[i]);
    }

    int n;
    scanf("%d", &n);

    char a[100];
    scanf("%s", a);

    char b[100];
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
