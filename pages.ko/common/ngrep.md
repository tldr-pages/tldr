# ngrep

> 정규식을 사용하여 네트워크 트래픽 패킷을 필터링.
> 더 많은 정보: <https://github.com/jpr5/ngrep/blob/master/EXAMPLES.md>.

- 모든 인터페이스의 트래픽 캡처:

`ngrep -d any`

- 특정 인터페이스의 트래픽 캡처:

`ngrep -d {{eth0}}`

- 인터페이스 eth0의 포트 22를 지나는 트래픽 캡처:

`ngrep -d {{eth0}} port {{22}}`

- 특정 호스트로부터 또는 특정 호스트로 가는 트래픽 캡처:

`ngrep host {{www.example.com}}`

- 인터페이스 eth0의 'User-Agent:' 키워드 필터링:

`ngrep -d {{eth0}} '{{User-Agent:}}'`
