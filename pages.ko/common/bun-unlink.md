# bun unlink

> 현재 디렉토리를 링크 가능한 패키지로 등록 해제.
> 관련 항목: `bun link`.
> 더 많은 정보: <https://bun.com/docs/pm/cli/link#unlinking>.

- 현재 패키지를 전역에서 등록 해제:

`bun unlink`

- 특정 디렉토리의 패키지 등록 해제:

`bun unlink --cwd {{경로/대상/패키지}}`

- 실제로 등록 해제하지 않고 시뮬레이션(dry-run) 실행:

`bun unlink --dry-run`

- 도움말 표시:

`bun unlink {{[-h|--help]}}`
