#define _crt_secure_no_warnings

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

unsigned int init(){
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
    return alarm(0x1f);
}


int main() {
    int i, a, b, ans, op;
    char opc[4] = { '+', '-', '*', '/' };
    init();
    srand(time(NULL));
    printf("WELCOME TO hye0ngseok's MATH GAME\n");
    printf("If you beat hye0ngseok, you can find the FLAG.\n");
    printf("May God's blessing be with you\n");
    sleep(5);
    system("clear");

    for (i = 1; i < 101; i++) {
        a = rand() % 10000;
        b = rand() % 10000;
        op = rand() % 4;
        printf("[hye0ngseok HP:%d] %d %c %d = ?\n", 101-i, a, opc[op], b);
        printf(">>> ");
        scanf("%d", &ans);
        if (op == 0) {
            if (a + b == ans) {
                continue;
            }
            else {
                printf("NARAK!\n");
                return 0;
            }
        }

        if (op == 1) {
            if (a - b == ans) {
                continue;
            }
            else {
                printf("NARAK!\n");
                return 0;
            }
        }
        
        if (op == 2) {
            if (a * b == ans) {
                continue;
            }
            else {
                printf("NARAK!\n");
                return 0;
            }
        }

        if (op == 3) {
            if (a / b == ans) {
                continue;
            }
            else {
                printf("NARAK!\n");
                return 0;
            }
        }
    }
        printf("hye0ngseok is down! The FLAG is KCTFjr{METE0R_the_9i4nt_METE0R}");
        sleep(10);
}
