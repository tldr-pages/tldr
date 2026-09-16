# jj rebase

> 리비전을 다른 부모 리비전으로 이동.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-rebase>.

- 지정한 리비전을 다른 부모 리비전으로 이동:

`jj rebase {{[-r|--revisions]}} {{revset}} {{[-d|--destination]}} {{revset}}`

- 지정한 리비전과 모든 자식 리비전을 다른 부모 리비전으로 이동:

`jj rebase {{[-s|--source]}} {{revset}} {{[-d|--destination]}} {{revset}}`

- 지정한 리비전이 포함된 브랜치의 모든 리비전을 다른 부모 리비전으로 이동:

`jj rebase {{[-b|--branch]}} {{revset}} {{[-d|--destination]}} {{revset}}`

- 리비전을 다른 리비전의 앞이나 뒤로 이동:

`jj rebase {{[-r|--revisions]}} {{revset}} {{[-B|--insert-before]}} {{revset}} {{[-A|--insert-after]}} {{revset}}`
