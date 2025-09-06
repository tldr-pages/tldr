# calibre-server

> 네트워크를 통해 전자책을 배포하는 데 사용할 수 있는 서버 어플리케이션.
> 이전에 GUI 또는 보정기능을 사용하여 전자책을 라이브러리로 가져와야 함.
> Calibre 전자책 라이브러리의 일부.
> 더 많은 정보: <https://manual.calibre-ebook.com/generated/en/calibre-server.html>.

- 전자책을 배포할 서버 시작. <http://localhost:8080> 에 연결:

`calibre-server`

- 다른 포트에서 서버 시작. <http://localhost:port> 에 연결:

`calibre-server --port {{포트번호}}`

- 서버를 암호로 보호:

`calibre-server --username {{사용자이름}} --password {{비밀번호}}`
