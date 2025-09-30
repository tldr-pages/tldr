# npm adduser

> 레지스트리 사용자 계정 추가.
> 더 많은 정보: <https://docs.npmjs.com/cli/npm-adduser>.

- 지정된 레지스트리에 새 사용자 생성하고 자격 증명을 `.npmrc`에 저장:

`npm adduser --registry {{레지스트리_주소}}`

- 특정 범위로 개인 레지스트리에 로그인:

`npm login --scope {{@조직}} --registry {{https://registry.mycorp.com}}`

- 특정 범위에서 로그아웃하고 인증 토큰 제거:

`npm logout --scope {{@조직}}`

- 초기화 중 범위가 지정된 패키지 생성:

`npm init --scope {{@foo}} {{--yes}}`
