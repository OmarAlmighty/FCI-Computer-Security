#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_PASSWORD_LENGTH 256
#define FLAG_FILE "flag.txt"

// Hardcoded SHA-256 hash of the password "1qaz2wsx"
const char *correct_hash = "059a00192592d5444bc0caad7203f98b506332e2cf7abb35d684ea9bf7c18f08";

// Function to compute the SHA-256 hash of the user's input using the system's OpenSSL
int compute_sha256_with_openssl(const char *input, char *output_hash) {
    char command[MAX_PASSWORD_LENGTH + 50];
    FILE *fp;

    // Create the command to run the OpenSSL SHA-256 digest
    snprintf(command, sizeof(command), "echo -n \"%s\" | openssl dgst -sha256", input);

    // Run the command and get the result
    fp = popen(command, "r");
    if (fp == NULL) {
        perror("Failed to run openssl command");
        return -1;
    }

    // Read the output (it should be in the form of SHA256(stdin)= <hash>)
    if (fgets(output_hash, 65, fp) == NULL) {
        fclose(fp);
        return -1;
    }

    // Remove the "SHA256(stdin)= " part of the output
    char *hash_start = strchr(output_hash, '=') + 2; // Skip "SHA256(stdin)= "
    if (hash_start == NULL) {
        fclose(fp);
        return -1;
    }

    // Copy the actual hash into the output
    strncpy(output_hash, hash_start, 64);
    output_hash[64] = '\0'; // Ensure it's null-terminated
    
    fclose(fp);
    return 0;
}

int main() {
    char input_password[MAX_PASSWORD_LENGTH];
    FILE *flag_file;
    char flag[1024];  // Buffer to store flag content
    char user_hash[65]; // To store the hash computed by OpenSSL
    char my_hash[25];
    
    for (int i = 0; i < 24; i++)
        my_hash[i] = correct_hash[i];
    
    my_hash[24] = '\0';
    
    // Prompt the user for the password
    printf("Enter password: ");
    fgets(input_password, MAX_PASSWORD_LENGTH, stdin);

    // Remove the newline character that fgets might leave at the end
    input_password[strcspn(input_password, "\n")] = 0;

    // Compute the SHA-256 hash of the user's input using the system's OpenSSL
    if (compute_sha256_with_openssl(input_password, user_hash) != 0) {
        fprintf(stderr, "Error in OpenSSL\n");
        return 1;
    }

    // Compare the computed hash with the stored hash
    if (strcmp(user_hash, my_hash) == 0) {
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
    } else {
        printf("Incorrect password.\n");
    }

    return 0;
}
