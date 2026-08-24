# bun update

> Bun 프로젝트의 의존성을 업데이트.
> 더 많은 정보: <https://bun.com/docs/pm/cli/update>.

- 모든 의존성 업데이트:

`bun update`

- 호환성과 관계없이, 최신 버전으로 업데이트:

`bun update --latest`

- 특정 의존성 업데이트:

`bun update {{패키지_이름}}`

- 특정 버전으로 의존성 업데이트:

`bun update {{패키지_이름}}@{{버전}}`

- 대화형 모드로 의존성 업데이트:

`bun update {{[-i|--interactive]}}`

- 모든 워크스페이스에 대해 재귀적으로 의존성 업데이트:

`bun update {{[-r|--recursive]}}`

- 대화형 및 재귀 모드로 의존성 업데이트:

`bun update {{[-i|--interactive]}} {{[-r|--recursive]}}`
