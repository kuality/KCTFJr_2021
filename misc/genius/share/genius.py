#! /usr/bin/python3
from random import *

randint(1,20)
_list = ['*','+']

def main():
    print('We learned that addition has higher priority than multiplication.')
    print('then, can you solve the math problems with the formula?')

    a = 0
    for i in range(3,100,2):
        a+=1
        print(f"ROUND {a}!!")

        text = ""
        for j in range(i):
            if(j & 1):
                text += _list[randint(0,1)]
            else:
                text += str(randint(1,i**3))
        print(text)
        text = '('+text.replace('*',')*(').replace('+','+')+')'
        answer = int(input())
        if(answer != eval(text)):
            return 0
    print('Congratulation!!\n')
    print('Flag is KCTF{Y0U_AR6_5o_G6nius!!!!!!!!}')

if __name__=="__main__":
    main()