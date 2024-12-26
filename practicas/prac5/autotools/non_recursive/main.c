#include <stdio.h>
#include <stdlib.h>
#include "sum.h"


int main(int argc, char **argv) {
    if (argc != 3) {
        printf("Usage: %s <first_int> <second_int>\n", argv[0]);
        return 1;
    }

    int a = atoi(argv[1]);
    int b = atoi(argv[2]);
    int result = a + b;
    printf("sum using the API: %d\n", result);

    return 0;
}