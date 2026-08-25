# jj diffedit

> diff 편집기를 사용하여 리비전의 변경 내용을 수정.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-diffedit>.

- diff 편집기로 현재 리비전의 변경 내용 수정:

`jj diffedit`

- 지정한 리비전의 변경 내용 수정:

`jj diffedit {{[-r|--revision]}} {{revset}}`

- 두 리비전 간의 변경 내용을 비교하며 수정:

`jj diffedit {{[-f|--from]}} {{시작_revset}} {{[-t|--to]}} {{끝_revset}}`

- 지정한 경로의 변경 내용만 수정 (일치하지 않는 경로는 변경되지 않음):

`jj diffedit {{filesets}}`

- 지정한 diff 편집기 사용:

`jj diffedit --tool {{이름}}`

- 자식 리비전을 리베이스할 때 diff 대신 내용 유지:

`jj diffedit --restore-descendants`
