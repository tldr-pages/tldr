# proxify

> HTTP/HTTPS 트래픽을 캡처, 조작 및 재생할 수 있는 범용 프록시 도구.
> 관련 항목: `mitmproxy`.
> 더 많은 정보: <https://github.com/projectdiscovery/proxify#usage>.

- HTTP 프록시 시작 (루프백 인터페이스 `127.0.0.1`, 포트 `8888`):

`proxify`

- 사용자 지정 네트워크 인터페이스와 포트에서 HTTP 프록시 시작 (`1024` 미만 포트는 `sudo`가 필요할 수 있음):

`proxify {{[-ha|-http-addr]}} "{{ip_주소}}:{{포트_번호}}"`

- Specify output format and output file:

`proxify {{[-of|-output-format]}} {{jsonl|yaml}} {{[-o|-output]}} {{경로/대상/파일}}`

- 도움말 표시:

`proxify -h`
