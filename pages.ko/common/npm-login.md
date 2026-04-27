# npm login

> 레지스트리 사용자 계정에 로그인.
> 관련 항목: `npm logout`.
> 더 많은 정보: <https://docs.npmjs.com/cli/npm-login/>.

- 레지스트리 계정에 로그인하고 인증 정보를 `.npmrc` 파일에 저장:

`npm login`

- 사용자 정의 레지스트리로 로그인:

`npm login --registry {{레지스트리_주소}}`

- 특정 인증 방식으로 로그인:

`npm login --auth-type {{legacy|web}}`
