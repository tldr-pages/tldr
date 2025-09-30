# lwp-request

> 간단한 명령줄 HTTP 클라이언트.
> libwww-perl로 제작되었습니다.
> 더 많은 정보: <https://metacpan.org/pod/lwp-request>.

- 간단한 GET 요청 만들기:

`lwp-request -m GET {{http://example.com/some/path}}`

- 파일을 POST 요청으로 업로드:

`lwp-request -m POST {{http://example.com/some/path}} < {{경로/대상/파일}}`

- 사용자 지정 에이전트로 요청 만들기:

`lwp-request -H 'User-Agent: {{사용자_에이전트}} -m {{METHOD}} {{http://example.com/some/path}}`

- HTTP 인증으로 요청 만들기:

`lwp-request -C {{사용자이름}}:{{비밀번호}} -m {{METHOD}} {{http://example.com/some/path}}`

- 요청 헤더를 출력하며 요청 만들기:

`lwp-request -U -m {{METHOD}} {{http://example.com/some/path}}`

- 응답 헤더와 상태 체인을 출력하며 요청 만들기:

`lwp-request -E -m {{METHOD}} {{http://example.com/some/path}}`
