# pee

> `stdin`을 파이프로 전달하는 도구.
> 같이 보기: `tee`.
> 더 많은 정보: <https://manned.org/pee>.

- 각 명령을 실행하고, 각 명령에 `stdin`의 별도 복사본 제공:

`pee {{명령1 명령2 ...}}`

- `stdin`의 복사본을 `stdout`에 쓰기 (`tee`처럼 동작):

`pee cat {{명령1 명령2 ...}}`

- SIGPIPE 및 쓰기 오류 발생 시 즉시 종료:

`pee --no-ignore-sigpipe --no-ignore-write-errors {{명령1 명령2 ...}}`
