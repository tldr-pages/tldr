# xh

> 친숙하고 빠른 HTTP 요청 전송 도구.
> 참고: Rust로 작성된 `xh`는 `http`의 효과적인 대체 도구입니다.
> 같이 보기: `http`, `curl`.
> 더 많은 정보: <https://github.com/ducaale/xh>.

- GET 요청 전송:

`xh {{httpbin.org/get}}`

- JSON 본문과 함께 POST 요청 전송 (키-값 쌍이 최상위 JSON 객체에 추가됨, 예: `{"name": "john", "age": 25}`):

`xh post {{httpbin.org/post}} {{name=john}} {{age:=25}}`

- 쿼리 매개변수를 포함한 GET 요청 전송 (예: `first_param=5&second_param=true`):

`xh get {{httpbin.org/get}} {{first_param==5}} {{second_param==true}}`

- 사용자 지정 헤더와 함께 GET 요청 전송:

`xh get {{httpbin.org/get}} {{header-name:header-value}}`

- GET 요청을 보내고 응답 본문을 파일에 저장:

`xh --download {{httpbin.org/json}} --output {{경로/대상/파일}}`

- 동등한 `curl` 명령 표시 (이 명령은 요청을 전송하지 않음):

`xh --{{curl|curl-long}} {{--follow --verbose get http://example.com user-agent:curl}}`
