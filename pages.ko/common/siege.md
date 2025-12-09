# siege

> HTTP 부하 테스트 및 벤치마킹 도구.
> 더 많은 정보: <https://www.joedog.org/siege-manual/>.

- 기본 설정으로 URL 테스트:

`siege {{https://example.com}}`

- URL 목록 테스트:

`siege --file {{경로/대상/url_목록.txt}}`

- URL 목록을 무작위 순서로 테스트 (인터넷 트래픽 시뮬레이션):

`siege --internet --file {{경로/대상/url_목록.txt}}`

- URL 목록 벤치마킹 (요청 사이에 대기하지 않음):

`siege --benchmark --file {{경로/대상/url_목록.txt}}`

- 동시 연결 수 설정:

`siege --concurrent={{50}} --file {{경로/대상/url_목록.txt}}`

- 실행 시간 설정:

`siege --time={{30s}} --file {{경로/대상/url_목록.txt}}`
