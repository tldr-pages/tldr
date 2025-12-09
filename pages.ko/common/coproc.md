# coproc

> 대화형 비동기 서브셸을 생성하기 위한 내장 Bash.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#Coprocesses>.

- 서브셸을 비동기적으로 실행:

`coproc { {{명령어1; 명령어2; ...}}; }`

- 특정 이름을 가진 보조 프로세스를 만듬:

`coproc {{이름}} { {{명령어1; 명령어2; ...}}; }`

- 특정 보조 프로세스 `stdin`에 쓰기:

`echo "{{입력}}" >&"${{{이름}}[1]}"`

- 특정 보조 프로세스 `stdout`에서 읽음:

`read {{변수}} <&"${{{이름}}[0]}"`

- `stdin`을 반복적으로 읽고 입력에 대해 일부 명령을 실행하는 보조 프로세스를 만듬:

`coproc {{이름}} { while read line; do {{명령어1; 명령어2; ...}}; done }`

- `bc`를 실행하는 보조 프로세스를 만들고 사용:

`coproc BC { bc --mathlib; }; echo "1/3" >&"${BC[1]}"; read output <&"${BC[0]}"; echo "$output"`
