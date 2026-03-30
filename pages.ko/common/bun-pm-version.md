# bun pm version

> `package.json`의 `version` 필드를 관리.
> 더 많은 정보: <https://bun.com/docs/pm/cli/pm#version>.

- 현재 패키지 버전 출력:

`bun pm version`

- 특정 버전으로 설정:

`bun pm version {{9.0.1}}`

- 시맨틱 버전 규칙(`major`, `minor`, `patch` 등)에 따라 버전 증가:

`bun pm version {{major|minor|patch|premajor|preminor|prepatch|prerelease}}`

- Git 태그를 기준으로 버전 설정:

`bun pm version from-git`
