# jj new

> 새로운 빈 변경을 생성.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-new>.

- 현재 리비전 위에 새 빈 변경 생성:

`jj new`

- 지정한 리비전 위에 새 빈 변경 생성:

`jj new {{revision}}`

- 여러 리비전 위에 새 병합 변경 생성:

`jj new {{revset1 revset2 ...}}`

- 지정한 리비전의 앞과 뒤에 새 빈 변경 생성:

`jj new {{[-B|--insert-before]}} {{revsets}} {{[-A|--insert-after]}} {{revsets}}`
