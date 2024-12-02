#include <stdio.h>
#include <unistd.h>
#define FLAG_FILE "flag.txt"

//************Compile it***********************
// cat /proc/sys/kernel/randomize_va_space 
// echo 0 > /proc/sys/kernel/randomize_va_space
// gcc -fno-stack-protector crackme6.c -o crackme6
//********************************************

int print_flag(char secret, char array[]){
    FILE *flag_file;
    char flag[1024];  // Buffer to store flag content
    secret += 3;
    if (secret == 'H') {
        // Open the flag file
        flag_file = fopen(FLAG_FILE, "r");
        if (flag_file == NULL) {
            fprintf(stderr, "Error: Could not open %s\n", FLAG_FILE);
            return 1;
        }

        // Read and print the flag file
        printf("Access granted. Here is your flag:\n");
        while (fgets(flag, sizeof(flag), flag_file) != NULL) {
            printf("%s", flag);  // Output the flag content
        }

        fclose(flag_file);
        return 0;
    }else{
        printf("%s\n", array);

    }

    // Print user input
    printf("Get out of here!\n");
    return 0;
}

int main() {

    // Define variables
    char array[120];
    char secret = 'B';

    // Grab user input
    printf("Who are you:\n");
    // fgets(array, 400, stdin);
    gets(array);

    print_flag(secret, array);


    // Return success
    return 0;
}

// cat /proc/sys/kernel/randomize_va_space 
// echo 0 > /proc/sys/kernel/randomize_va_space
// gcc -fno-stack-protector -z execstack -mpreferred-stack-boundary=4 -o example -ggdb example.c