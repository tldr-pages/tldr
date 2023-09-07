# ab

> 아파치 벤치마킹 도구.
> 로드 테스트를 수행하는 가장 간단한 도구.
> 더 많은 정보: <https://httpd.apache.org/docs/current/programs/ab.html>.

- 지정된 URL에 대해 100개의 HTTP GET 요청 실행:

`ab -n {{100}} {{url}}`

- 지정된 URL에 대해 100개의 HTTP GET 요청을 최대 10개의 요청을 동시에 처리하며 실행:

`ab -n {{100}} -c {{10}} {{url}}`

- 지정된 파일의 JSON 페이로드를 사용하여 URL에 대해 100개의 HTTP POST 요청 실행:

`ab -n {{100}} -T {{application/json}} -p {{경로/대상/파일.json}} {{url}}`

- HTTP [K]eep Alive 사용, 즉 하나의 HTTP 세션 내에서 여러 요청을 수행:

`ab -k {{url}}`

- 벤치마킹에 사용될 최대 시간(초) 설정:

`ab -t {{60}} {{url}}`
