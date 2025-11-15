# indent

> C/C++ 프로그램의 공백을 삽입하거나 삭제하여 외형을 변경합니다.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/indent.1.html>.

- Berkeley 스타일에 따라 C/C++ 소스 코드 서식 지정:

`indent {{경로/대상/소스_파일.c}} {{경로/대상/서식화된_파일.c}} -nbad -nbap -bc -br -c33 -cd33 -cdb -ce -ci4 -cli0 -di16 -fc1 -fcb -i4 -ip -l75 -lp -npcs -nprs -psl -sc -nsob -ts8`

- Kernighan & Ritchie (K&R) 스타일에 따라 C/C++ 소스 코드 서식 지정:

`indent {{경로/대상/소스_파일.c}} {{경로/대상/서식화된_파일.c}} -nbad -bap -nbc -br -c33 -cd33 -ncdb -ce -ci4 -cli0 -cs -d0 -di1 -nfc1 -nfcb -i4 -nip -l75 -lp -npcs -nprs -npsl -nsc -nsob`
