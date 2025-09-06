# promtool

> Prometheus 모니터링 시스템을 위한 도구.
> 더 많은 정보: <https://prometheus.io/docs/prometheus/latest/getting_started/>.

- 구성 파일이 유효한지 여부 확인 (오류가 있을 경우 보고):

`promtool check config {{구성_파일.yml}}`

- 규칙 파일이 유효한지 여부 확인 (오류가 있을 경우 보고):

`promtool check rules {{규칙_파일.yml}}`

- `stdin`을 통해 Prometheus 메트릭을 전달하여 일관성과 정확성을 확인:

`curl --silent {{http://example.com:9090/metrics/}} | promtool check metrics`

- 규칙 구성에 대한 단위 테스트:

`promtool test rules {{테스트_파일.yml}}`
