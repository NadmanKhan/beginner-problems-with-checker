#include <stdio.h>

int main() {

    long long x, y;
    scanf("%lld %lld", &x, &y);
    printf("%d\n", x + y); // wrong format specifier

    return 0;
}