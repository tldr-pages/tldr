# type

> 셀이 실행할 명령의 유형을 표시합니다.
> 참고: 모든 예시는 POSIX 호환이 아닙니다.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-type>.

- 명령의 유형 표시:

`type {{명령어}}`

- 지정된 실행 파일을 포함하는 모든 위치 표시 (Bash/fish/Zsh 셸에서만 작동):

`type -a {{명령어}}`

- 실행될 디스크 파일의 이름 표시 (Bash/fish/Zsh 셸에서만 작동):

`type -p {{명령어}}`

- 특정 명령, 별칭/키워드/함수/내장 명령/파일의 유형 표시 (Bash/fish 셸에서만 작동):

`type -t {{명령어}}`
