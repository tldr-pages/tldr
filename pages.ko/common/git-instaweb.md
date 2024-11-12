# git instaweb

> GitWeb 서버를 실행하는 도우미 도구.
> 더 많은 정보: <https://git-scm.com/docs/git-instaweb>.

- 현재 Git 저장소에 대해 GitWeb 서버 실행:

`git instaweb --start`

- 로컬호스트에서만 리슨:

`git instaweb --start --local`

- 특정 포트에서 리슨:

`git instaweb --start --port {{1234}}`

- 지정된 HTTP 데몬 사용:

`git instaweb --start --httpd {{lighttpd|apache2|mongoose|plackup|webrick}}`

- 웹 브라우저도 자동으로 실행:

`git instaweb --start --browser`

- 현재 실행 중인 GitWeb 서버 중지:

`git instaweb --stop`

- 현재 실행 중인 GitWeb 서버 재시작:

`git instaweb --restart`
