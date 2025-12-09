# chronic

> 명령이 실패한 경우에만 명령의 `stdout` 및 `stderr`를 표시.
> 더 많은 정보: <https://manned.org/chronic>.

- 0이 아닌 종료 코들드를 생성하거나 충돌하는 경우에만 지정된 명령의 `stdout` 및 `stderr`을 표시:

`chronic {{명령어 옵션 ...}}`

- 비어있지 않은 `stderr`을 생성하는 경우에만 지정된 명령의 `stdout` 및 `stderr`을 표시:

`chronic -e {{명령어 옵션 ...}}`

- 상세([v]erbose) 모드 활성화:

`chronic -v {{명령어 옵션 ...}}`
