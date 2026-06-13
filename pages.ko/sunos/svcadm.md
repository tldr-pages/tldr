# svcadm

> 서비스 인스턴스를 조작합니다.
> 더 많은 정보: <https://www.unix.com/man-page/linux/1m/svcadm>.

- 서비스를 서비스 데이터베이스에서 활성화:

`svcadm enable {{서비스_이름}}`

- 서비스 비활성화:

`svcadm disable {{서비스_이름}}`

- 실행 중인 서비스 다시 시작:

`svcadm restart {{서비스_이름}}`

- 서비스에게 구성 파일을 다시 읽도록 명령:

`svcadm refresh {{서비스_이름}}`

- 서비스의 유지보수 상태를 해제하고 시작하도록 명령:

`svcadm clear {{서비스_이름}}`
