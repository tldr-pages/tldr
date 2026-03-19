# dirs

> 디렉토리 스택을 표시하거나 조작.
> 디렉토리 스택은 `pushd`과 `popd` 명령어로 조작할 수 있는 최근 방문한 디렉토리의 목록이다.
> 관련 항목: `pushd`, `popd`.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#Directory-Stack-Builtins>.


- 디렉토리 스택을 각 항목 사이에 공백을 두고 출력:

`dirs`

- 디렉토리 스택을 한 줄에 하나씩 출력:

`dirs -p`

- 디렉토리 스택을 번호가 붙은 목록으로 출력:

`dirs -v`

- 틸드(`~`) 접두어 없이 디렉토리 스택 출력:

`dirs -l`

- 디렉토리 스택에서 `n`번째 항목만 출력 (0부터 시작, Bash 전용):

`dirs +{{n}}`

- 디렉토리 스택의 마지막부터 `n`번째 항목만 출력 (0부터 시작, Bash 전용):

`dirs -{{n}}`

- 디렉토리 스택 비우기:

`dirs -c`
