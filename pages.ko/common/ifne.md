# ifne

> `stdin`의 비어 있음에 따라 명령을 실행.
> 더 많은 정보: <https://manned.org/ifne>.

- `stdin`이 비어 있지 않은 경우에만 지정된 명령을 실행:

`ifne {{명령어 옵션 ...}}`

- `stdin`이 비어 있는 경우에만 지정된 명령을 실행하고, 그렇지 않으면 `stdin`을 `stdout`에 전달:

`ifne -n {{명령어 옵션 ...}}`
