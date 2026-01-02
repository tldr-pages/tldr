# gdb

> GNU 디버거.
> 더 많은 정보: <https://sourceware.org/gdb/current/onlinedocs/gdb#Invocation>.

- 실행파일을 디버깅합니다:

`gdb {{실행파일}}`

- 프로세스를 gdb에 연결합니다:

`gdb {{[-p|--pid]}} {{프로세스ID}}`

- 코어 파일과 함께 디버깅합니다:

`gdb {{[-c|--core]}} {{코어}} {{실행파일}}`

- 디버깅을 시작하면서 주어진 GDB 명령들을 수행합니다:

`gdb {{[-ex|--eval-command]}} "{{명령들}}" {{실행파일}}`

- 디버깅을 시작하면서 실행파일에 인자들을 넘겨줍니다:

`gdb --args {{실행파일}} {{인자1}} {{인자2}}`
