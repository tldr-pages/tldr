# jj duplicate

> 기존 변경(Change)과 동일한 내용을 가진 새 변경(Change)을 생성.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-duplicate>.

- 현재 리비전을 기존 부모 리비전 위에 복제:

`jj duplicate`

- 지정한 리비전을 기존 부모 리비전 위에 복제:

`jj duplicate {{revset}}`

- 지정한 리비전을 다른 부모 리비전 위에 복제:

`jj duplicate {{[-d|--destination]}} {{대상_revset}} {{revset}}`

- 지정한 리비전을 다른 리비전 뒤에 삽입하여 복제:

`jj duplicate {{[-A|--insert-after]}} {{다른_revset}} {{revset}}`

- 지정한 리비전을 다른 리비전 앞에 삽입하여 복제:

`jj duplicate {{[-B|--insert-before]}} {{이전_revset}} {{revset}}`

- 여러 부모 리비전 위에 복제 (병합 커밋 생성):

`jj duplicate {{[-d|--destination]}} {{목적지1}} {{[-d|--destination]}} {{목적지2}} {{revset}}`

- 여러 리비전 복제:

`jj duplicate {{revset1 revset2 ...}}`
