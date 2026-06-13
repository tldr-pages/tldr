# adig

> 도메인 네임 시스템(DNS) 서버에서 받은 정보를 출력합니다.
> 더 많은 정보: <https://manned.org/adig>.

- 호스트 이름에 대한 A (기본) 레코드를 DNS에서 표시:

`adig {{example.com}}`

- 추가 [d]디버깅 출력 표시:

`adig -d {{example.com}}`

- 특정 DNS [s]서버에 연결:

`adig -s {{1.2.3.4}} {{example.com}}`

- DNS 서버에 연결할 때 특정 TCP 포트 사용:

`adig -T {{포트}} {{example.com}}`

- DNS 서버에 연결할 때 특정 UDP 포트 사용:

`adig -U {{포트}} {{example.com}}`
