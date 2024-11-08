# simplehttpserver

> 파일 업로드, 기본 인증, 사용자 정의 응답을 위한 YAML 규칙을 지원하는 간단한 HTTP/S 서버.
> Python의 `http.server`에 대한 Go 대안.
> 더 많은 정보: <https://github.com/projectdiscovery/simplehttpserver>.

- 현재 디렉토리를 제공하며 모든 인터페이스와 포트 8000에서 기본적으로 수신 대기하는 HTTP 서버 시작 (자세한 출력 포함):

`simplehttpserver -verbose`

- 모든 인터페이스에서 포트 80을 통해 특정 경로를 제공하며 기본 인증을 사용하는 HTTP 서버 시작:

`sudo simplehttpserver -basic-auth {{사용자명}}:{{비밀번호}} -path {{/var/www/html}} -listen 0.0.0.0:80`

- 자체 서명된 인증서와 사용자 정의 SAN을 사용하여 HTTPS를 활성화하며 모든 인터페이스에서 HTTP 서버 시작:

`sudo simplehttpserver -https -domain {{*.selfsigned.com}} -listen 0.0.0.0:443`

- 사용자 정의 응답 헤더와 업로드 기능을 사용하여 HTTP 서버 시작:

`simplehttpserver -upload -header '{{X-Powered-By: Go}}' -header '{{Server: SimpleHTTPServer}}'`

- YAML에서 사용자 정의 가능한 규칙을 사용하여 HTTP 서버 시작 (DSL에 대한 문서 참조):

`simplehttpserver -rules {{규칙.yaml}}`
