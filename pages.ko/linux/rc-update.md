# rc-update

> OpenRC 서비스를 실행 수준에 추가 및 제거.
> 같이 보기: `openrc`.
> 더 많은 정보: <https://manned.org/rc-update>.

- 모든 서비스와 추가된 실행 수준 나열:

`rc-update show`

- 서비스를 실행 수준에 추가:

`sudo rc-update add {{서비스_이름}} {{실행_수준}}`

- 실행 수준에서 서비스 제거:

`sudo rc-update delete {{서비스_이름}} {{실행_수준}}`

- 모든 실행 수준에서 서비스 제거:

`sudo rc-update --all delete {{서비스_이름}}`
