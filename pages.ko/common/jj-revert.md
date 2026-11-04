# jj revert

> 지정한 리비전의 변경 사항을 되돌리는 역변경을 적용.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-revert>.

- 지정한 revset의 변경 사항을 되돌리는 역변경 적용 (예: `B::D`, `A..D`, `B|C|D` 등):

`jj revert {{[-r|--revisions]}} {{revsets}}`

- 지정한 리비전 위에 역변경 적용:

`jj revert {{[-r|--revisions]}} {{revsets}} {{[-d|--destination]}} {{revsets}}`

- 지정한 리비전의 앞이나 뒤에 역변경 적용:

`jj revert {{[-r|--revisions]}} {{revsets}} {{[-B|--insert-before]}} {{revsets}} {{[-A|--insert-after]}} {{revsets}}`
