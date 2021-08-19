#include <stdio.h>
#include <stdlib.h>

unsigned int init(){
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
    return alarm(0x1f);
}

int main(){

    char answer;
    init();
    puts("We're FSB. We need your help.\n");
    puts("Are you hacker?\n");
    puts("Answer Y or N.\n");
    
    read(0,&answer,1);
    while (getchar() != '\n');
    if(answer == 'Y' || answer == 'y'){

        Enermy_program();
       
    }
    else{
        puts("Sorry. bye.");
        exit(0);
    }
    
   
}

void Enermy_program(){
    
    char buffer[100];
    puts("Good. We have the enermy's program. Check this.\n");
    puts("This Code is Something different. Maybe That is key point.\n");
    puts("\n---------------------------enermy's program----------------------------\n");
        
    puts("Tong shin bo an. Here is BBu GGu gi!\n");
    puts("Do you hear me?\n");
       
    read(0, buffer, 100);
    printf(buffer);

    puts("-----------------------------------------------------------------------\n");

}
void vuln(){
    system("/bin/sh");
}