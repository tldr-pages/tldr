# bun link

> 로컬 패키지를 링크 가능한 상태로 등록하거나, 등록된 패키지를 프로젝트에 연결.
> 관련 항목: `bun unlink`.
> 더 많은 정보: <https://bun.com/docs/pm/cli/link>.

- 현재 패키지를 전역으로 링크:

`bun link`

- 패키지를 프로젝트에 로컬로 링크:

`bun link {{패키지_이름}}`

- 특정 디렉토리에 있는 패키지를 링크:

`bun link --cwd {{경로/대상/패키지}}`

- 실제로 링크하지 않고 시뮬레이션(dry run)만 진행:

`bun link --dry-run`

- 도움말 출력:

`bun link {{[-h|--help]}}`
