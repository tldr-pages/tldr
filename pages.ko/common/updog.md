# updog

> Python의 SimpleHTTPServer를 대체하는 도구.
> HTTP/S를 통해 업로드와 다운로드를 지원하며, 임시 SSL 인증서를 설정하고 HTTP 기본 인증을 사용할 수 있습니다.
> 더 많은 정보: <https://github.com/sc0tfree/updog>.

- 현재 디렉토리에 대한 HTTP 서버 시작:

`updog`

- 지정된 디렉토리에 대한 HTTP 서버 시작:

`updog --directory {{/경로/대상/폴더}}`

- 지정된 포트에서 HTTP 서버 시작:

`updog --port {{포트}}`

- 비밀번호를 사용하여 HTTP 서버 시작 (로그인 시 사용자 이름을 비워두고 비밀번호 필드에 비밀번호 입력):

`updog --password {{비밀번호}}`

- SSL을 통한 전송 암호화 활성화:

`updog --ssl`
