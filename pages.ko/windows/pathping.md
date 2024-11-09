# pathping

> `ping` 및 `tracert`의 기능을 결합한 라우팅 도구입니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/pathping>.

- 호스트에 핑을 보내고 경로를 추적:

`pathping {{호스트명}}`

- 호스트명을 IP 주소로 역방향 조회하지 않음:

`pathping {{호스트명}} -n`

- 대상을 찾기 위해 검색할 최대 홉 수 지정 (기본값은 30):

`pathping {{호스트명}} -h {{최대_홉}}`

- 핑 사이에 대기할 시간 지정 (기본값은 240):

`pathping {{호스트명}} -p {{시간}}`

- 각 홉에 대한 쿼리 수 지정 (기본값은 100):

`pathping {{호스트명}} -q {{쿼리}}`

- IPv4 사용 강제:

`pathping {{호스트명}} -4`

- IPv6 사용 강제:

`pathping {{호스트명}} -6`

- 도움말 표시:

`pathping /?`
