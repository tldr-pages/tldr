# bun outdated

> 최신 버전이 존재하는 의존성 목록을 확인.
> 더 많은 정보: <https://bun.com/docs/pm/cli/outdated>.

- 현재 프로젝트의 모든 오래된 의존성 목록 출력:

`bun outdated`

- 특정 패키지가 오래되었는지 확인:

`bun outdated {{패키지}}`

- glob 패턴에 일치하는 오래된 의존성 목록 출력:

`bun outdated "{{패턴}}"`

- 특정 워크스페이스에 대한 오래된 의존성 목록 출력 :

`bun outdated {{[-F|--filter]}} "{{작업공간_패턴}}"`

- 모노레포의 모든 워크스페이스를 재귀적으로 검사:

`bun outdated {{[-r|--recursive]}}`
