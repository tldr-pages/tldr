# torify

> 네트워크 트래픽을 Tor 네트워크를 통해 라우팅.
> 참고: 이 명령은 더 이상 사용되지 않으며, 이제 `torsocks`의 하위 호환 래퍼입니다.
> 더 많은 정보: <https://manned.org/torify>.

- 트래픽을 Tor를 통해 라우팅:

`torify {{명령}}`

- 셸에서 Tor 토글:

`torify {{on|off}}`

- Tor 사용 셸 생성:

`torify --shell`

- Tor 사용 셸 확인:

`torify show`

- Tor 설정 파일 지정:

`torify -c {{설정_파일}} {{명령}}`

- 특정 Tor SOCKS 프록시 사용:

`torify -P {{프록시}} {{명령}}`

- 출력 결과를 파일로 리다이렉트:

`torify {{명령}} > {{경로/대상/출력}}`
