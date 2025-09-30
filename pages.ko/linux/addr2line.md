# addr2line

> 바이너리의 주소를 파일 이름과 줄 번호로 변환.
> 더 많은 정보: <https://manned.org/addr2line>.

- 실행 파일의 명령어 주소로부터 소스 코드의 파일 이름과 줄 번호 표시:

`addr2line --exe={{경로/대상/실행_파일}} {{주소}}`

- 함수 이름, 파일 이름 및 줄 번호 표시:

`addr2line --exe={{경로/대상/실행_파일}} --functions {{주소}}`

- C++ 코드의 함수 이름 디맹글링:

`addr2line --exe={{경로/대상/실행_파일}} --functions --demangle {{주소}}`
