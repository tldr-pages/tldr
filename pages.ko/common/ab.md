# ab

> 아파치 벤치마킹 도구.
> 로드 테스트를 수행하는 가장 간단한 도구.
> 더 많은 정보: <https://httpd.apache.org/docs/2.4/programs/ab.html>.

- 주어진 URL에 대해 100개의 HTTP GET 요청 실행:

`ab -n {{100}} {{url}}`

- 지정된 URL에 대해 최대 10개의 요청을 동시에 처리하여 100개의 HTTP GET을 실행:

`ab -n {{100}} -c {{10}} {{url}}`

- 생존을 유지하며 사용:

`ab -k {{url}}`

- 벤치마킹에 사용될 최대 시간(초) 설정:

`ab -t {{60}} {{url}}`
