# http_load

> HTTP 벤치마킹 도구.
> 웹 서버의 처리량을 테스트하기 위해 여러 HTTP 패치를 병렬로 실행합니다.
> 더 많은 정보: <https://www.acme.com/software/http_load/>.

- 초당 20개의 요청을 주어진 URL 목록 파일을 기반으로 60초 동안 에뮬레이트:

`http_load -rate {{20}} -seconds {{60}} {{경로/대상/urls.txt}}`

- 5개의 동시 요청을 주어진 URL 목록 파일을 기반으로 60초 동안 에뮬레이트:

`http_load -parallel {{5}} -seconds {{60}} {{경로/대상/urls.txt}}`

- 초당 20개의 요청으로 1000개의 요청을 주어진 URL 목록 파일을 기반으로 에뮬레이트:

`http_load -rate {{20}} -fetches {{1000}} {{경로/대상/urls.txt}}`

- 5개의 동시 요청으로 1000개의 요청을 주어진 URL 목록 파일을 기반으로 에뮬레이트:

`http_load -parallel {{5}} -fetches {{1000}} {{경로/대상/urls.txt}}`
