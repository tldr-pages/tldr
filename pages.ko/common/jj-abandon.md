# jj abandon

> 리비전을 폐기하고, 해당 리비전의 자식 리비전들을 부모 리비전으로 리베이스.
> 리비전을 폐기하면 연결된 변경 ID(Change ID)도 함께 제거.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-abandon>.

- 지정한 revset의 리비전 폐기 (예: `B::D`, `A..D`, `B|C|D` 등):

`jj abandon {{revsets}}`

- 북마크는 삭제하지 않고 부모 리비전으로 이동한 상태에서, 리비전 폐기:

`jj abandon --retain-bookmarks {{revsets}}`

- 자식 리비전의 내용을 변경하지 않고 리비전 폐기:

`jj abandon --restore-descendants {{revsets}}`
