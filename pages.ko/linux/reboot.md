# reboot

> 시스템을 재부팅합니다.
> 더 많은 정보: <https://manned.org/reboot.8>.

- 시스템 재부팅:

`reboot`

- 시스템 전원 끄기 (`poweroff`와 동일):

`reboot {{[-p|--poweroff]}}`

- 시스템 중지 (모든 프로세스를 종료하고 CPU를 셧다운) (`halt`와 동일):

`reboot --halt`

- 시스템 관리자를 거치지 않고 즉시 재부팅:

`reboot {{[-f|--force]}}`

- 시스템을 재부팅하지 않고 wtmp 종료 항목 기록:

`reboot {{[-w|--wtmp-only]}}`
