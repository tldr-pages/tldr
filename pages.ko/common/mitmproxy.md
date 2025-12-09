# mitmproxy

> 대화형 중간자 HTTP 프록시.
> 같이 보기: `mitmweb` 및 `mitmdump`.
> 더 많은 정보: <https://docs.mitmproxy.org/stable/>.

- 기본 설정으로 `mitmproxy` 시작 (포트 `8080`에서 대기):

`mitmproxy`

- 사용자 정의 주소와 포트에 바인딩하여 `mitmproxy` 시작:

`mitmproxy --listen-host {{IP_주소}} {{[-p|--listen-port]}} {{포트}}`

- 스크립트를 사용하여 트래픽을 처리하는 `mitmproxy` 시작:

`mitmproxy {{[-s|--scripts]}} {{경로/대상/script.py}}`

- SSL/TLS 마스터 키로 로그를 외부 프로그램(와이어샤크 등)으로 내보내기:

`SSLKEYLOGFILE="{{경로/대상/파일}}" mitmproxy`

- 프록시 서버의 작동 모드 지정 (`regular`가 기본값):

`mitmproxy {{[-m|--mode]}} {{regular|transparent|socks5|...}}`

- 콘솔 레이아웃 설정:

`mitmproxy --console-layout {{horizontal|single|vertical}}`
