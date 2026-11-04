# jj split

> 하나의 리비전을 두 개로 분할.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-split>.

- 지정한 리비전을 대화형으로 두 개로 분할하고, 두 번째 리비전을 첫 번째 리비전 위에 생성:

`jj split {{[-r|--revision]}} {{revision}}`

- 지정한 리비전에서 일치하는 파일만 분리하여 새 리비전 생성:

`jj split {{[-r|--revision]}} {{revision}} {{fileset}}`

- 지정한 리비전을 분할하고, 두 번째 리비전을 지정한 대상 리비전 위에 생성:

`jj split {{[-r|--revision]}} {{revision}} {{[-d|--destination]}} {{revset}}`

- 지정한 리비전을 분할하고, 두 번째 리비전을 다른 리비전의 앞이나 뒤에 생성:

`jj split {{[-r|--revision]}} {{revision}} {{[-B|--insert-before]}} {{revset}} {{[-A|--insert-after]}} {{revset}}`

- 지정한 리비전을 두 개의 병렬 리비전으로 분할:

`jj split {{[-r|--revision]}} {{revision}} {{[-p|--parallel]}}`
