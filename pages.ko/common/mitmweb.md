# mitmweb

> 웹 기반의 대화형 중간자(MITM) HTTP 프록시.
> 같이 보기: `mitmproxy`.
> 더 많은 정보: <https://docs.mitmproxy.org/stable/concepts-options>.

- 기본 설정으로 `mitmweb` 시작:

`mitmweb`

- 사용자 지정 주소와 포트로 `mitmweb` 시작:

`mitmweb --listen-host {{IP_주소}} --listen-port {{포트}}`

- 트래픽을 처리하기 위해 스크립트를 사용하여 `mitmweb` 시작:

`mitmweb --scripts {{경로/대상/스크립트.py}}`
