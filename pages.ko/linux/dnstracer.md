# dnstracer

> dnstracer 명령은 DNS가 정보를 어디서 얻는지 확인합니다.
> 더 많은 정보: <https://manned.org/dnstracer>.

- 로컬 DNS가 www.example.com에 대한 정보를 어디서 얻었는지 확인:

`dnstracer {{www.example.com}}`

- 이미 알고 있는 특정 DNS에서 시작:

`dnstracer -s {{dns.example.org}} {{www.example.com}}`

- IPv4 서버만 쿼리:

`dnstracer -4 {{www.example.com}}`

- 실패 시 각 요청을 5번 재시도:

`dnstracer -r {{5}} {{www.example.com}}`

- 실행 중 모든 단계 표시:

`dnstracer -v {{www.example.com}}`

- 실행 후 수신된 모든 응답의 개요 표시:

`dnstracer -o {{www.example.com}}`
