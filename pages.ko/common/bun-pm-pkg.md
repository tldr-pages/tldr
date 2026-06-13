# bun pm pkg

> `get`, `set`, `delete`, `fix` 작업을 통해 package.json 데이터를 관리.
> 더 많은 정보: <https://bun.com/docs/pm/cli/pm#pkg>.

- `package.json`의 모든 속성 조회:

`bun pm pkg get`

- 특정 속성 하나 조회:

`bun pm pkg get {{속성}}`

- 여러 속성 조회:

`bun pm pkg get {{속성1 속성2 속성3 ...}}`

- 중첩된 속성 조회:

`bun pm pkg get {{속성}}.{{attribute}}`

- 속성 설정:

`bun pm pkg set {{속성}}="{{값}}"`

- 속성 삭제:

`bun pm pkg delete {{속성}}`

- `package.json`의 일반적인 문제를 자동으로 수정:

`bun pm pkg fix`
