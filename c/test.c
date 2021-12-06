#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int *open_file(const char *filename) {
    
    FILE *data_file = fopen(filename,"r");
    char line;
    size_t linesize = 0;

    static int numberArray[20000];
    int counter = 0;
    int buffer[4];
    int buf_count = 0;

    while( (line = fgetc(data_file)) != EOF ) {
        // printf("%c",line);

        // put the number into the array
        if (line = '\n') {
            buffer[buf_count++] = line;
        }
        else {
            buf_count = 0;
            numberArray[counter++] = buffer;
        }
    }
    // free(line);
    fclose(data_file);
    return numberArray;
}


int main() {
    printf("This is working!\n");
    int *numbers;
    numbers = open_file("../data/day1.txt");
    printf("\n\n");
    // printf("%d\n", numbers[0]);
    for(int n=0; n<20000; n++) {
        int x = numbers[n];
        if ((x != 0) && (n <= 2)) {
            printf("%c",x);
        }
    }

    return 0;
}