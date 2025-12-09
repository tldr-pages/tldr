# nethogs

> 프로세스별 대역폭 사용량 모니터링.
> 더 많은 정보: <https://manned.org/nethogs>.

- 루트 권한으로 NetHogs 시작 (기본 장치는 `eth0`):

`sudo nethogs`

- 특정 장치의 대역폭 모니터링:

`sudo nethogs {{장치}}`

- 여러 장치의 대역폭 모니터링:

`sudo nethogs {{장치1}} {{장치2}}`

- 새로 고침 주기 지정:

`sudo nethogs -t {{초}}`
