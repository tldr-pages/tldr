# coproc

> 상호작용 비동기 하위 셸을 생성하기 위한 Bash 내장 명령어.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#Coprocesses>.

- 하위 셸을 비동기적으로 실행:

`coproc { {{명령어1; 명령어2; ...}}; }`

- 특정 이름으로 보조 프로세스 생성:

`coproc {{이름}} { {{명령어1; 명령어2; ...}}; }`

- 특정 보조 프로세스의 `stdin`에 쓰기:

`echo "{{입력}}" >&"${{{이름}}[1]}"`

- 특정 보조 프로세스의 `stdout`에서 읽기:

`read {{변수}} <&"${{{이름}}[0]}"`

- `stdin`을 계속 읽고 입력에 대해 명령어를 실행하는 보조 프로세스 생성:

`coproc {{이름}} { while read line; do {{명령어1; 명령어2; ...}}; done }`

- `stdin`을 계속 읽고 입력에 대해 파이프 라인을 실행하고 출력을 `stdout`에 쓰는 보조 프로세스 생성:

`coproc {{이름}} { while read line; do echo "$line" | {{명령어1 | 명령어2 | ...}} | cat /dev/fd/0; done }`

- `bc`를 실행하는 보조 프로세스를 생성하고 사용:

`coproc BC { bc --mathlib; }; echo "1/3" >&"${BC[1]}"; read output <&"${BC[0]}"; echo "$output"`
