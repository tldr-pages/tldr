# nettop

> 네트워크에 대한 업데이트된 정보를 표시합니다.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/nettop.1.html>.

- 모든 인터페이스의 TCP 및 UDP 소켓 모니터링:

`nettop`

- 루프백 인터페이스의 TCP 소켓 모니터링:

`nettop -m {{tcp}} -t {{loopback}}`

- 특정 프로세스 모니터링:

`nettop -p "{{프로세스_ID|프로세스_이름}}"`

- 프로세스별 요약 표시:

`nettop -P`

- 네트워크 정보의 10개의 샘플 출력:

`nettop -l {{10}}`

- 5초마다 변경 사항 모니터링:

`nettop -d -s {{5}}`

- nettop 실행 중 상호작용 명령 나열:

`<h>`

- 도움말 표시:

`nettop -h`
