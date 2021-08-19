# Yes! or Yes!

문제설명 : 올바른 입력값을 찾아내시오.

파일명 : reversing_#1

### 풀이

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  signed int i; // [rsp+Ch] [rbp-94h]
  char v5[136]; // [rsp+10h] [rbp-90h]
  unsigned __int64 v6; // [rsp+98h] [rbp-8h]

  v6 = __readfsqword(0x28u);
  gets(v5, argv, envp);
  for ( i = 0; i <= 22; ++i )
  {
    if ( flag[i] != ((unsigned __int8)v5[i] ^ 0xE) )
    {
      puts("NO!NO!NO!");
      exit(0);
    }
  }
  puts("GREAT!!!");
  return 0;
}
```

입력을 받고 입력값과 0xe와 XOR 연산을 하여 flag와 `MZHu\KX=\?@IQ]>>AQKT/s`  1byte씩 비교한다. 만약 다르다면 프로그램이 종료되고, 조건을 다 통과한다면 "GREAT"라는 문자열을 출력해준다. 따라서 `MZHu\KX=\?@IQ]>>AQKT/s`  문자열 1byte씩 0xe를 다시 XOR연산을 한다면 "GREAT" 문자열이 출력되는 입력값을 알 수 있을 것이다.

```c
#include <stdio.h>
#include <string.h>

int main(){
    char check[] = "EMZHu\\KX=\\?@IQ]>>AQKT/s";
    char flag[128];

    for(int i =0; i < 23; i++){
        printf("%c", check[i] ^ 0x0e);
    }

    printf("%s\n", flag);
}
```



FLAG : KCTF{REV3R1NG_S00O_EZ!}