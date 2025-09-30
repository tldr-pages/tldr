# ufw

> 간단한 방화벽.
> 방화벽 구성을 더욱 쉽게 만들어주는 `iptables`의 프론트엔드.
> 더 많은 정보: <https://wiki.ubuntu.com/UncomplicatedFirewall>.

- ufw 활성화:

`ufw enable`

- ufw 비활성화:

`ufw disable`

- 번호와 함께 ufw 규칙 표시:

`ufw status numbered`

- 이 호스트의 포트 5432에서 서비스 식별 주석과 함께 들어오는 트래픽 허용:

`ufw allow {{5432}} comment "{{Service}}"`

- 192.168.0.4에서 이 호스트의 모든 주소로의 포트 22에서 TCP 트래픽만 허용:

`ufw allow proto {{tcp}} from {{192.168.0.4}} to {{any}} port {{22}}`

- 이 호스트의 포트 80에서 트래픽 차단:

`ufw deny {{80}}`

- 포트 범위 8412:8500에 대한 모든 UDP 트래픽 차단:

`ufw deny proto {{udp}} from {{any}} to {{any}} port {{8412:8500}}`

- 특정 규칙 삭제. 규칙 번호는 `ufw status numbered` 명령으로 확인 가능:

`ufw delete {{규칙_번호}}`
