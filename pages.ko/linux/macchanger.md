# macchanger

> 네트워크 인터페이스 MAC 주소를 조작하는 명령줄 유틸리티.
> 더 많은 정보: <https://manned.org/macchanger>.

- 인터페이스의 현재 및 영구 MAC 주소 보기:

`macchanger --show {{인터페이스}}`

- 인터페이스를 임의의 MAC으로 설정:

`macchanger --random {{인터페이스}}`

- 인터페이스를 임의의 MAC 주소로 설정하고, [b]urned-[i]n-[a]ddress로 가장:

`macchanger --random --bia {{인터페이스}}`

- 인터페이스를 특정 MAC 주소로 설정:

`macchanger --mac {{XX:XX:XX:XX:XX:XX}} {{인터페이스}}`

- 알려진 모든 공급업체의 식별자(MAC 주소의 처음 세 바이트) 출력:

`macchanger --list`

- 인터페이스를 영구 하드웨어 MAC 주소로 재설정:

`macchanger --permanent {{인터페이스}}`
