#include <stdio.h>
#include <stdlib.h>

unsigned int init(){
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
    return alarm(0x1f);
}

int main(){
    
    init();
    puts("Catch me if You can!\n");
    puts("You have to pass Two stages to catch me. Good luck.\n");


    stage1();
    
    
}

void stage1(){

    char buf[125];

    puts("welcome! here is stage1.\n");
    puts("You can go next stage if you clear mission.\n");
    puts("Explain the mission. Overwrite Return Address with stage2 address. hint: Buffer Overflow..\n");

    puts("Attack me.\n");
    
    read(0, buf, 0x100);
    
}

void stage2(){
    
    int v1 = 0xaaaabbbb;
    int v2 = 0xaaaabbbb;
    int magic_number = 0xdeadbeef;
    int v3 = 0xaaaabbbb;
    char buf2[16];

    puts("Attack me: ");
    gets(buf2);

    if(magic_number == 0xcafebabe){
        puts("You win.\n");
        system("/bin/sh");

    }


}
