# halt

> 시스템을 중지합니다.
> 더 많은 정보: <https://manned.org/halt.8>.

- 시스템 중지:

`halt`

- 시스템 전원 끄기 (`poweroff`와 동일):

`halt {{[-p|--poweroff]}}`

- 시스템 재부팅 (`reboot`와 동일):

`halt --reboot`

- 시스템 관리자와 상의하지 않고 즉시 중지:

`halt {{[-f|--force]}}`

- 시스템을 중지하지 않고 wtmp 종료 항목 작성:

`halt {{[-w|--wtmp-only]}}`
