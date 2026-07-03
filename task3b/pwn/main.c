#include <stdio.h>
#include <stdlib.h>

void win() {
    printf("\n----FLAG----\n");
    printf("CTF{buffer_overflow_success}\n");
}

void vulnerable() {
    char buffer[64];

    printf("Enter your name: ");

    gets(buffer); 

    printf("Hello %s ...\n", buffer);
}

int main() {
    vulnerable();
    return 0;
}