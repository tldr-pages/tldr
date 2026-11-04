# jj squash

> 한 리비전의 변경 사항을 다른 리비전으로 이동.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-squash>.

- 현재 리비전의 모든 변경 사항을 부모 리비전으로 이동:

`jj squash`

- 지정한 리비전의 모든 변경 사항을 부모 리비전으로 이동:

`jj squash {{[-r|--revision]}} {{revset}}`

- 지정한 리비전의 모든 변경 사항을 다른 리비전으로 이동:

`jj squash {{[-f|--from]}} {{revsets}} {{[-t|--into]}} {{revset}}`

- 스쿼시할 변경 사항을 대화형으로 선택:

`jj squash {{[-i|--interactive]}}`
