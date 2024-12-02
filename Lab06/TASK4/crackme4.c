#include <stdio.h>
#include <string.h>

#define TARGET_STRING "RVS]cV>=(B,1YF+2#x"

int main() {
    char input[18], transformed[18];

    // Read the input string
    printf("Tell me a secret: ");
    scanf("%s", input);

    int i;
    for (i = 0; i < 18; i++) {
        transformed[i] = (input[i] - i) ^ 20 ;
        // Compare the transformed string with the target string
        if (transformed[i] != TARGET_STRING[i]) {
            printf("Not good!\n");
            return 1;
        } 
    }
    printf("That's GOOD!\n");
    

    return 0;
}