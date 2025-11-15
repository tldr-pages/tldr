# strace

> 시스템 호출을 추적하는 문제 해결 도구.
> 더 많은 정보: <https://manned.org/strace>.

- 특정 [p]프로세스를 PID로 추적 시작:

`strace {{[-p|--attach]}} {{pid}}`

- [p]프로세스를 추적하고 시스템 호출로 출력을 필터링:

`strace {{[-p|--attach]}} {{pid}} -e {{system_call,system_call2,...}}`

- 각 시스템 호출에 대해 시간, 호출 횟수, 오류 수를 계산하고 프로그램 종료 시 요약 보고:

`strace {{[-p|--attach]}} {{pid}} {{[-c|--summary-only]}}`

- 각 시스템 호출에 소요된 [T]시간을 표시하고 출력할 문자열 최대 크기 지정:

`strace {{[-p|--attach]}} {{pid}} {{[-T|--syscall-times]}} {{[-s|--string-limit]}} {{32}}`

- 프로그램을 실행하여 추적 시작:

`strace {{프로그램}}`

- 파일 작업을 추적 시작:

`strace -e trace=file {{프로그램}}`

- 프로그램의 네트워크 작업과 모든 [f]포크된 및 자식 프로세스를 추적하고 [o]출력을 파일에 저장:

`strace {{[-f|--follow-forks]}} -e trace=network {{[-o|--output]}} {{추적.txt}} {{프로그램}}`
