#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        return 1;
    }

    //create a text file, write the summarized text into it
    FILE *file = fopen("summary_output.txt", "w");
    if (file == NULL) {
        printf("Unable to open file\n");
        return 1;
    }

    for (int i = 1; i < argc; i++) {
        fprintf(file, "%s ", argv[i]);
    }

    fclose(file);
    printf("Summary has been written to summary_output.txt\n");

    return 0;
}
