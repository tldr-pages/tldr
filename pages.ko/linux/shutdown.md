# shutdown

> 시스템 종료 및 재부팅.
> 더 많은 정보: <https://manned.org/shutdown.8>.

- 즉시 전원 끄기 ([h]alt):

`shutdown -h now`

- 즉시 [r]재부팅:

`shutdown {{[-r|--reboot]}} now`

- 5분 후 [r]재부팅:

`shutdown {{[-r|--reboot]}} +{{5}} &`

- 오후 1시에 종료하기 (24시간 [h] 형식 사용):

`shutdown -h 13:00`

- 보류 중인 종료/재부팅 작업 [c]취소:

`shutdown -c`
