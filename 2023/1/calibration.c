#include <stdio.h>
#include <stdlib.h>

#define LEN 100000

int main()
{
    FILE *fptr = fopen("filename.txt", "r");
    char *in = malloc(LEN * sizeof (char));
    fgets(in, LEN, fptr);

    for (int i = 0; i < LEN && *(in + i) != '\0'; ++i) {
        int a = 10, b;
        while (*(in + i) != '\n') {
            if ('0' <= *(in + i) && *(in + i) <= '9') {
                if (a == 10) {
                    
                }
            }
        }
    }

    fclose(fptr);
    free(in);
}
