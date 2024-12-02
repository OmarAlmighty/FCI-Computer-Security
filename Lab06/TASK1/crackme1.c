#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_PASSWORD_LENGTH 256
#define FLAG_FILE "flag.txt"

int main() {
    char input_password[MAX_PASSWORD_LENGTH];
    const char *correct_password = "SuperSecretPassword";  // Hardcoded password
    FILE *flag_file;
    char flag[1024];  // Buffer to store flag content

    // Prompt the user for the password
    printf("Enter password: ");
    fgets(input_password, MAX_PASSWORD_LENGTH, stdin);

    // Remove newline character that fgets might leave at the end
    input_password[strcspn(input_password, "\n")] = 0;

    // Check if the entered password is correct
    if (strcmp(input_password, correct_password) == 0) {
        // Open the flag file
        flag_file = fopen(FLAG_FILE, "r");
        if (flag_file == NULL) {
            fprintf(stderr, "Error: Could not open %s\n", FLAG_FILE);
            return 1;
        }

        // Read the flag file
        printf("Access granted. Here is your flag:\n");
        while (fgets(flag, sizeof(flag), flag_file) != NULL) {
            printf("%s", flag);  // Output the flag content
        }

        fclose(flag_file);
    } else {
        printf("Incorrect password.\n");
    }

    return 0;
}
