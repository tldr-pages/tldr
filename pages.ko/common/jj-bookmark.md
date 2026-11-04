# jj bookmark

> `jj` 저장소의 북마크를 관리.
> Git 백엔드를 사용하는 경우, 북마크는 Git 브랜치에 해당.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-bookmark>.

- 지정한 리비전에 새로운 북마크 생성:

`jj {{[b|bookmark]}} {{[c|create]}} {{[-r|--revision]}} {{리비전}} {{이름}}`

- 모든 북마크와 대상 리비전 목록 표시:

`jj {{[b|bookmark]}} {{[l|list]}}`

- 기존 북마크를 다른 리비전으로 이동:

`jj {{[b|bookmark]}} {{[m|move]}} {{[-t|--to]}} {{리비전}} {{이름}}`

- 지정한 원격 북마크 추적:

`jj {{[b|bookmark]}} {{[t|track]}} {{이름}}@{{원격}}`

- 북마크를 삭제하고, 다음 push 시 원격 저장소에도 삭제 사항 전파:

`jj {{[b|bookmark]}} {{[d|delete]}} {{이름}}`

- push 시 삭제를 전파하지 않고, 로컬에서만 북마크 제거:

`jj {{[b|bookmark]}} {{[f|forget]}} {{이름}}`
