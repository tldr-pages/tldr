# resend

> 명령줄에서 이메일을 전송하고 관리.
> 더 많은 정보: <https://github.com/resend/resend-cli#commands>.

- Resend에 로그인 (인증을 위해 브라우저 열기):

`resend login`

- API 키를 직접 사용하여 로그인 (for CI/agents):

`resend login --key {{re_xxxxxxxxx}}`

- 이메일 전송:

`resend emails send --from {{email@example.com}} --to {{recipient@example.com}} --subject "{{대상}}" --text "{{메시지}}"`

- 템플릿 생성:

`resend templates create --name "{{Welcome}}" --subject "{{대상}}" --html "{{<h1>Hello</h1>}}"`

- 템플릿을 사용하여 이메일 전송:

`resend emails send --to {{recipient@example.com}} --template {{템플릿_아이디}}`

- 인증된 도메인 목록 표시:

`resend domains {{[ls|list]}}`

- 현재 인증 상태 표시:

`resend whoami`

- CLI 버전, API 키 및 도메인 상태 확인:

`resend doctor`
