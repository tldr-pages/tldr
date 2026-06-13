# http-prompt

> 자동 완성 및 구문 강조 기능을 갖춘 대화형 명령줄 HTTP 클라이언트.
> 더 많은 정보: <https://github.com/httpie/http-prompt>.

- 기본 URL <http://localhost:8000> 또는 이전 세션을 대상으로 세션 시작:

`http-prompt`

- 지정된 URL로 세션 시작:

`http-prompt {{http://example.com}}`

- 초기 옵션과 함께 세션 시작:

`http-prompt {{localhost:8000/api}} --auth {{사용자명:비밀번호}}`
