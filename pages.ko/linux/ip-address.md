# ip address

> IP 주소 관리 하위 명령어.
> 더 많은 정보: <https://manned.org/ip-address>.

- 네트워크 인터페이스와 해당 IP 주소 나열:

`ip {{[a|address]}}`

- 활성 네트워크 인터페이스만 표시하도록 필터링:

`ip {{[a|address]}} {{[s|show]}} up`

- 특정 네트워크 인터페이스에 대한 정보 표시:

`ip {{[a|address]}} {{[s|show]}} {{eth0}}`

- 네트워크 인터페이스에 IP 주소 추가:

`sudo ip {{[a|address]}} {{[a|add]}} {{ip_주소}} dev {{eth0}}`

- 네트워크 인터페이스에서 IP 주소 제거:

`sudo ip {{[a|address]}} {{[d|delete]}} {{ip_주소}} dev {{eth0}}`

- 지정된 범위의 모든 IP 주소를 네트워크 인터페이스에서 삭제:

`sudo ip {{[a|address]}} {{[f|flush]}} {{eth0}} scope {{global|host|link}}`
