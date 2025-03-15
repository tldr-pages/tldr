# protonvpn connect

> ProtonVPN에 연결.
> 더 많은 정보: <https://github.com/Rafficer/linux-cli-community>.

- ProtonVPN에 대화식으로 연결:

`protonvpn {{[c|connect]}}`

- 사용 가능한 가장 빠른 서버로 ProtonVPN에 연결:

`protonvpn {{[c|connect]}} {{[-f|--fastest]}}`

- 특정 서버와 특정 프로토콜로 ProtonVPN에 연결:

`protonvpn {{[c|connect]}} {{서버_이름}} -p {{udp|tcp}}`

- 임의의 서버와 특정 프로토콜로 ProtonVPN에 연결:

`protonvpn {{[c|connect]}} {{[-r|--random]}} -p {{udp|tcp}}`

- Tor를 지원하는 가장 빠른 서버로 ProtonVPN에 연결:

`protonvpn {{[c|connect]}} --tor`

- 도움말 표시:

`protonvpn connect --help`
