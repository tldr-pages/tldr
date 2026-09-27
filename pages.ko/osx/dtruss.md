# dtruss

> DTrace를 사용하여 `osx`의 시스템 호출과 커널 동작을 추적.
> 참고: 시스템 무결성 보호를 비활성화해야 함.
> 관련 항목: `strace`.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/dtruss.1m.html>.

- PID를 지정하여 실행 중인 프로세스 추적:

`sudo dtruss -p {{프로세스_아이디}}`

- 프로그램을 실행하고 시스템 호출 추적:

`sudo dtruss {{프로그램}}`

- 지정한 이름과 일치하는 프로세스를 기다렸다가([W]ait) 추적:

`sudo dtruss -W {{이름}}`

- 각 시스템 호출의 경과 시간([e]lapsed time), CPU 실행시간([o]n-cpu time), 호출 횟수([c]ount) 출력:

`sudo dtruss -eoc -p {{프로세스_아이디}}`

- 프로세스와 해당 자식 프로세스를 함께 추적([f]ollow):

`sudo dtruss -f -p {{프로세스_아이디}}`

- 지정한 시스템 호출의 발생 내역 출력:

`sudo dtruss -t {{syscall}} -p {{프로세스_아이디}}`
