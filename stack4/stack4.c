#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void win() {
    printf("code flow successfully changed\n");
}

int main(int argc, char **argv) {
    char buffer[64];

    gets(buffer);
}