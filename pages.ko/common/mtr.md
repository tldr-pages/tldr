# mtr

> Matt's Traceroute: 트레이서라우트와 핑 도구를 결합한 도구.
> 더 많은 정보: <https://manned.org/mtr>.

- 호스트로 트레이서라우트를 수행하고 모든 중간 홉을 지속적으로 핑:

`mtr {{example.com}}`

- IP 주소 및 호스트 이름 매핑 비활성화:

`mtr --no-dns {{example.com}}`

- 각 홉을 10번씩 핑한 후 출력 생성:

`mtr --report-wide {{example.com}}`

- IPv4 또는 IPv6 강제 사용:

`mtr -4 {{example.com}}`

- 동일한 홉에 또 다른 패킷을 보내기 전 주어진 시간(초) 대기:

`mtr --interval {{10}} {{example.com}}`

- 각 홉에 대한 자율 시스템 번호(ASN) 표시:

`mtr --aslookup {{example.com}}`

- IP 주소와 역방향 DNS 이름 모두 표시:

`mtr --show-ips {{example.com}}`
