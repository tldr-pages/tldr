# jj interdiff

> 두 리비전 간 변경 사항을 비교.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-interdiff>.

- 지정한 리비전과 작업 복사본의 변경 사항 비교:

`jj interdiff {{[-f|--from]}} {{revset}}`

- 지정한 두 리비전의 변경 사항 비교:

`jj interdiff {{[-f|--from]}} {{시작_revset}} {{[-t|--to]}} {{끝_revset}}`

- 지정한 경로의 변경 사항만 비교:

`jj interdiff {{[-f|--from]}} {{시작_revset}} {{[-t|--to]}} {{끝_revset}} {{filesets}}`

- 변경 사항 요약 표시:

`jj interdiff {{[-f|--from]}} {{revset}} {{[-s|--summary]}}`

- 변경 사항 통계 표시:

`jj interdiff {{[-f|--from]}} {{revset}} --stat`

- Git 형식의 diff 표시:

`jj interdiff {{[-f|--from]}} {{revset}} --git`

- 색상만으로 변경 사항을 표시하는 단어 단위 diff 표시:

`jj interdiff {{[-f|--from]}} {{revset}} --color-words`
