#include <stdio.h>
#include <stdlib.h>

void win(){
    printf("You win~!~!!~!!!!!!");
    system("/bin/sh");
}

unsigned int init(){
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
    return alarm(0x1f);
}

int main(){

    int canary_cousin = 0xcafebabe;
    char buf[256];
    init();
    printf("Attack me without my knowing~~!~!!\n");
    
    gets(buf);

    if(canary_cousin != 0xcafebabe){

        printf("ar le ri col re ri\n");
        printf("Actually, I'm canary's cousin! Study more!\n");
        printf("Ah, I will kill this program now. bye @.@~~!!!\n");
        exit(0);
    }
}