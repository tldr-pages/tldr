# watchexec

> 파일이 변경될 때 임의의 명령을 실행.
> 더 많은 정보: <https://manned.org/watchexec>.

- 현재 디렉토리의 파일이 변경될 때 `ls -la` 실행:

`watchexec {{ls -la}}`

- 현재 디렉토리의 JavaScript, CSS, HTML 파일이 변경될 때 `make` 실행:

`watchexec --exts {{js,css,html}} make`

- `lib` 또는 `src` 디렉토리의 파일이 변경될 때 `make` 실행:

`watchexec --watch {{lib}} --watch {{src}} {{make}}`

- 현재 디렉토리의 파일이 변경될 때 `my_server` 호출/재시작, 자식 프로세스를 중지하기 위해 `SIGKILL` 신호 전송:

`watchexec --restart --stop-signal {{SIGKILL}} {{my_server}}`
