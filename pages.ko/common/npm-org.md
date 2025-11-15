# npm org

> 조직을 관리.
> 더 많은 정보: <https://docs.npmjs.com/cli/npm-org>.

- 조직에 새 사용자 추가:

`npm org set {{조직_이름}} {{사용자명}}`

- 조직 내 사용자의 역할 변경:

`npm org set {{조직_이름}} {{사용자명}} {{developer|admin|owner}}`

- 조직에서 사용자 제거:

`npm org rm {{조직_이름}} {{사용자명}}`

- 조직의 모든 사용자 나열:

`npm org ls {{조직_이름}}`

- 조직의 모든 사용자를 JSON 형식으로 나열:

`npm org ls {{조직_이름}} --json`

- 조직 내 사용자의 역할 표시:

`npm org ls {{조직_이름}} {{사용자명}}`
