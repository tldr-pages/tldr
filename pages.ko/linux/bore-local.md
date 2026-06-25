# bore local

> Bore를 사용해 로컬 프록시를 원격 서버에 연결.
> 더 많은 정보: <https://github.com/ekzhang/bore#detailed-usage>.

- 로컬 포트를 원격 Bore 서버에 노출:

`bore local {{[-t|--to]}} {{원격_서버_주소}} {{로컬_포트}}`

- `localhost` 대신 특정 로컬 호스트 노출:

`bore local {{[-l|--local-host]}} {{host}} {{[-t|--to]}} {{원격_서버_주소}} {{로컬_포트}}`

- 원격 서버 포트를 명시적으로 지정:

`bore local {{[-t|--to]}} {{원격_서버_주소}} {{[-p|--port]}} {{원격_포트}} {{로컬_포트}}`

- 인증용 시크릿 사용:

`bore local {{[-t|--to]}} {{원격_서버_주소}} {{[-s|--secret]}} {{당신의_시크릿}} {{로컬_포트}}`

- 도움말 표시:

`bore local {{[-h|--help]}}`
