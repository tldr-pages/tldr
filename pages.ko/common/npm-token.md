# npm token

> npm 레지스트리를 위한 인증 토큰을 관리하고 생성.
> 더 많은 정보: <https://docs.npmjs.com/cli/npm-token>.

- 새 인증 토큰 생성:

`npm token create`

- 계정과 연결된 모든 토큰 나열:

`npm token list`

- 특정 토큰 ID를 사용하여 토큰 삭제:

`npm token revoke {{토큰_id}}`

- 읽기 전용 액세스 권한을 가진 토큰 생성:

`npm token create --read-only`

- 게시 액세스 권한을 가진 토큰 생성:

`npm token create --publish`

- 로그인 시 글로벌 `.npmrc` 파일에 npm 토큰 자동 구성:

`npm login`

- 글로벌 구성에서 토큰 제거:

`npm token revoke {{토큰_id}}`
