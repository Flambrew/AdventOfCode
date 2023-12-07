#include <stdio.h>
#include <stdlib.h>

#define LEN 100000

int main()
{
    FILE *fptr = fopen("./2023/1/data", "r");
    char *in = malloc(LEN * sizeof(char));
    fgets(in, LEN, fptr);

    int sum = 0;
    for (int i = -1, a, b; ++i < LEN && in[i] != '\0'; sum += a * 10 + b) {
        a = 10;
        while (in[i] != '\n') {
            printf("%c ", in[i]);
            if ('0' <= in[i] && in[i] <= '9') {
                if (a == 10) {
                    a = b = (in[i] - '0');
                } else {
                    b = (in[i] - '0');
                }
            }
            i++;
        }
        printf("%d\n", sum);
    }

    printf("%d\n", sum);

    fclose(fptr);
    free(in);
}
