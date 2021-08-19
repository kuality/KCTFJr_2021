# RockYou

문제설명 : aespa의 사생팬들이 작당모의를 하고있다는 첩보와 주고받은 사진을 입수했다. 우리의 aespa를 지켜내자!

파일명 : MISC_#2.png

### 풀이

 ![MISC_#2](/Users/spark/Desktop/MISC_#2.png)

사진에 무언가 숨겨져있다는 것을 생각한다면 스테가노그래피가 생각날 것이다.

또한 rockyou 키워드를 통해서 사전대입공격의 password 모음 파일 rockyou.txt를 알아낼수 있다.

사전대입공격을 통해서 패스워드가 "playboy1"이라는 것을 알아낼수 있다.

 https://www.mobilefish.com/services/steganography/steganography.php

사진에서 숨겨둔 메모를 추출해보자.

`91)ZJHV&']0Q(6>BJX"51O+"K0f*u/0d1r` 를 추출할 수 있다.

인코딩되어있는 것을 알수있고, base85 디코딩을 통해 FLAG를 얻을 수 있다.



FLAG : KCTF{Im_0n_th3_n3xt_13v31!}