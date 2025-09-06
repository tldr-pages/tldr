# nslookup

> 다양한 도메인 레코드에 대해 네임 서버에 질의.
> 더 많은 정보: <https://manned.org/nslookup>.

- 시스템의 기본 네임 서버에 도메인의 IP 주소 (A 레코드) 질의:

`nslookup {{example.com}}`

- 주어진 네임 서버에 도메인의 NS 레코드 질의:

`nslookup -type=NS {{example.com}} {{8.8.8.8}}`

- IP 주소의 역방향 조회 (PTR 레코드) 질의:

`nslookup -type=PTR {{54.240.162.118}}`

- TCP 프로토콜을 사용하여 모든 사용 가능한 레코드 질의:

`nslookup -vc -type=ANY {{example.com}}`

- 주어진 네임 서버에 도메인의 전체 존 파일 (존 전송)을 TCP 프로토콜을 사용하여 질의:

`nslookup -vc -type=AXFR {{example.com}} {{네임_서버}}`

- 도메인의 메일 서버 (MX 레코드) 질의, 트랜잭션 세부사항 표시:

`nslookup -type=MX -debug {{example.com}}`

- 특정 포트 번호로 주어진 네임 서버에 도메인의 TXT 레코드 질의:

`nslookup -port={{포트_번호}} -type=TXT {{example.com}} {{네임_서버}}`
