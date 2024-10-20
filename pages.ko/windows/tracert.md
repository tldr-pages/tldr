# tracert

> 컴퓨터와 대상 사이의 경로에서 각 단계에 대한 정보를 받습니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/tracert>.

- 경로 추적:

`tracert {{IP}}`

- `tracert`가 IP 주소를 호스트 이름으로 확인하지 않도록 방지:

`tracert /d {{IP}}`

- `tracert`가 IPv4만 사용하도록 강제:

`tracert /4 {{IP}}`

- `tracert`가 IPv6만 사용하도록 강제:

`tracert /6 {{IP}}`

- 대상을 찾기 위한 검색에서 최대 홉 수 지정:

`tracert /h {{최대_홉_수}} {{IP}}`

- 도움말 표시:

`tracert /?`
