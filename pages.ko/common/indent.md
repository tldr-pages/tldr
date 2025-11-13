# indent

> 공백을 삽입하거나 삭제하여 a C/C++ 프로그램의 모양을 변경.
> 더 많은 정보: <https://www.gnu.org/software/indent/manual/indent/Option-Summary.html>.

- Linux 스타일 가이드에 따라 C/C++ 소스 형식을 지정하고, 원본 파일을 자동으로 백업한 후, 들여쓰기된 버전으로 변경:

`indent --linux-style {{경로/대상/소스.c}} {{경로/대상/또다른_소스.c}}`

- GNU 스타일에 따라 C/C++ 소스 형식을 지정하고, 들여쓰기된 버전을 다른 파일에 저장:

`indent --gnu-style {{경로/대상/소스.c}} -o {{경로/대상/들여쓰기된_소스.c}}`

- Kernighan & Ritchie (K&R) 스타일에 따라 C/C++ 소스 형식을 지정하고, 탭이 없으며, 들여쓰기당 공백 3개, 줄바꿈은 120자:

`indent --k-and-r-style --indent-level3 --no-tabs --line-length120 {{경로/대상/소스.c}} -o {{경로/대상/들여쓰기된_소스.c}}`
