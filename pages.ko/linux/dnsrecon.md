# dnsrecon

> DNS 열거 도구.
> 더 많은 정보: <https://github.com/darkoperator/dnsrecon>.

- 도메인을 스캔하고 결과를 SQLite 데이터베이스에 저장:

`dnsrecon --domain {{example.com}} --db {{경로/대상/데이터베이스.sqlite}}`

- 도메인을 스캔하며 네임서버를 지정하고 존 전송 수행:

`dnsrecon --domain {{example.com}} --name_server {{nameserver.example.com}} --type axfr`

- 도메인을 스캔하며 서브도메인 및 호스트명의 사전으로 무차별 공격 수행:

`dnsrecon --domain {{example.com}} --dictionary {{경로/대상/사전.txt}} --type brt`

- 도메인을 스캔하며 SPF 레코드에서 IP 범위의 역방향 조회를 수행하고 JSON 파일에 결과 저장:

`dnsrecon --domain {{example.com}} -s --json`

- 도메인을 스캔하며 Google 열거를 수행하고 CSV 파일에 결과 저장:

`dnsrecon --domain {{example.com}} -g --csv`

- 도메인을 스캔하며 DNS 캐시 스누핑 수행:

`dnsrecon --domain {{example.com}} --type snoop --name_server {{nameserver.example.com}} --dictionary {{경로/대상/사전.txt}}`

- 도메인을 스캔하며 존 워킹 수행:

`dnsrecon --domain {{example.com}} --type zonewalk`
