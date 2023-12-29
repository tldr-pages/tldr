# telnet

> telnet 프로토콜을 사용해 호스트의 특정 포트에 연결합니다.
> 더 많은 정보: <https://manned.org/telnet>.

- 호스트의 기본 포트에 Telnet 연결:

`telnet {{호스트}}`

- 호스트의 특정 포트에 Telnet 연결:

`telnet {{ip_주소}} {{포트}}`

- Telnet 세션 종료:

`quit`

- 세션 종료를 위한 기본 이스케이프 문자 조합을 전송:

`<Ctrl> + ]`

- "x"를 세션 종료 문자로 사용하여 세션 시작:

`telnet -e {{x}} {{ip_주소}} {{포트}}`

- Telnet 으로 스타워즈 보기:

`telnet {{towel.blinkenlights.nl}}`
