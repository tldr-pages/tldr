# http

> HTTPie: 테스트, 디버깅 및 일반적으로 API 및 HTTP 서버와 상호작용하도록 설계된 HTTP 클라이언트.
> 더 많은 정보: <https://httpie.io/docs/cli/usage>.

- 간단한 GET 요청을 수행 (응답 헤더 및 콘텐츠 표시):

`http {{https://example.org}}`

- 특정 출력 내용을 인쇄 (`H`: 요청 헤더, `B`: 요청 본문, `h`: 응답 헤더, `b`: 응답 본문, `m`: 응답 메타데이터):

`http {{[-p|--print]}} {{H|B|h|b|m|Hh|Hhb|...}} {{https://example.com}}`

- 요청을 보낼 때 HTTP 메소드를 지정하고 프록시를 사용하여 요청을 가로채기:

`http {{GET|POST|HEAD|PUT|PATCH|DELETE|...}} --proxy {{http|https}}:{{http://localhost:8080|socks5://localhost:9050|...}} {{https://example.com}}`

- `3xx` 리디렉션을 따르고 요청에 추가 헤더를 지정:

`http {{[-F|--follow]}} {{https://example.com}} {{'User-Agent: Mozilla/5.0' 'Accept-Encoding: gzip'}}`

- 다양한 인증 방법을 사용하여 서버에 인증:

`http {{[-a|--auth]}} {{username:password|token}} {{[-A|--auth-type]}} {{basic|digest|bearer}} {{GET|POST|...}} {{https://example.com/auth}}`

- 요청을 생성하지만, 보내지 않음 (모의 실행과 유사):

`http --offline {{GET|DELETE|...}} {{https://example.com}}`

- 지속적인 사용자 정의 헤더, 인증 자격 증명 및 쿠키에 대해 명명된 세션을 사용:

`http --session {{세션_이름|경로/대상/세션.json}} {{[-a|--auth]}} {{사용자명}}:{{비밀번호}} {{https://example.com/auth}} {{API-KEY:xxx}}`

- 양식에 파일을 업로드 (아래 예에서는 양식 필드가 `<input type="file" name="cv" />`라고 가정):

`http {{[-f|--form]}} {{POST}} {{https://example.com/upload}} {{cv@경로/대상/파일}}`
