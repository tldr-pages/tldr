# conntrack

> Netfilter 연결 추적 시스템과 상호작용합니다.
> 연결 흐름을 검색, 나열, 검사, 수정 및 삭제합니다.
> 더 많은 정보: <https://manned.org/conntrack>.

- 현재 추적 중인 모든 연결 나열:

`conntrack --dump`

- 연결 변경 사항의 실시간 이벤트 로그 표시:

`conntrack --event`

- 연결 변경 사항 및 관련 타임스탬프의 실시간 이벤트 로그 표시:

`conntrack --event -o timestamp`

- 특정 IP 주소에 대한 연결 변경 사항의 실시간 이벤트 로그 표시:

`conntrack --event --orig-src {{IP_주소}}`

- 특정 소스 IP 주소에 대한 모든 흐름 삭제:

`conntrack --delete --orig-src {{IP_주소}}`
