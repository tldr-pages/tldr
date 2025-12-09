# l2ping

> L2CAP 에코 요청을 보내고 응답을 받습니다.
> 더 많은 정보: <https://manned.org/l2ping>.

- 블루투스 장치에 핑:

`sudo l2ping {{mac_주소}}`

- 블루투스 장치에 역방향 핑:

`sudo l2ping -r {{mac_주소}}`

- 지정된 인터페이스에서 블루투스 장치에 핑:

`sudo l2ping -i {{hci0}} {{mac_주소}}`

- 지정된 크기의 데이터 패키지로 블루투스 장치에 핑:

`sudo l2ping -s {{바이트_수}} {{mac_주소}}`

- 블루투스 장치에 핑 플러드:

`sudo l2ping -f {{mac_주소}}`

- 블루투스 장치에 지정된 횟수만큼 핑:

`sudo l2ping -c {{횟수}} {{mac_주소}}`

- 요청 간의 지정된 지연으로 블루투스 장치에 핑:

`sudo l2ping -d {{초}} {{mac_주소}}`
