# systemd-run

> 프로그램을 일시적 범위 단위, 서비스 단위, 경로, 소켓 또는 타이머로 트리거된 서비스 단위로 실행.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-run.html>.

- 일시적 서비스를 시작:

`sudo systemd-run {{명령어}} {{인수1 인수2 ...}}`

- 현재 사용자의 서비스 관리자에서 (권한 없이) 일시적 서비스를 시작:

`systemd-run --user {{명령어}} {{인수1 인수2 ...}}`

- 사용자 정의 단위 이름과 설명을 사용하여 일시적 서비스를 시작:

`sudo systemd-run --unit={{이름}} --description={{문자열}} {{명령어}} {{인수1 인수2 ...}}`

- 종료 후 정리되지 않는 일시적 서비스와 사용자 정의 환경 변수를 사용하여 시작:

`sudo systemd-run --remain-after-exit --set-env={{이름}}={{값}} {{명령어}} {{인수1 인수2 ...}}`

- 주기적으로 일시적 서비스를 실행하는 일시적 타이머 시작 (캘린더 이벤트 형식은 `man systemd.time` 참조):

`sudo systemd-run --on-calendar={{캘린더_이벤트}} {{명령어}} {{인수1 인수2 ...}}`

- 터미널을 프로그램과 공유하여 상호작용 입력/출력을 허용하고 프로그램 종료 후 실행 세부정보를 유지:

`systemd-run --remain-after-exit --pty {{명령어}}`

- 프로세스의 속성 (예: CPUQuota, MemoryMax)을 설정하고 종료될 때까지 대기:

`systemd-run --property MemoryMax={{메모리_바이트}} --property CPUQuota={{CPU_시간_비율}}% --wait {{명령어}}`

- 셸 파이프라인에서 프로그램 사용:

`{{명령어1}} | systemd-run --pipe {{명령어2}} | {{명령어3}}`
