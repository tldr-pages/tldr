# mkcert

> 로컬에서 신뢰할 수 있는 개발 인증서 생성.
> 더 많은 정보: <https://github.com/FiloSottile/mkcert>.

- 시스템 신뢰 저장소에 로컬 CA 설치:

`mkcert -install`

- 주어진 도메인에 대한 인증서와 개인 키 생성:

`mkcert {{example.org}}`

- 여러 도메인에 대한 인증서와 개인 키 생성:

`mkcert {{example.org}} {{myapp.dev}} {{127.0.0.1}}`

- 주어진 도메인과 하위 도메인에 대한 와일드카드 인증서와 개인 키 생성:

`mkcert "{{*.example.it}}"`

- 로컬 CA 제거:

`mkcert -uninstall`
