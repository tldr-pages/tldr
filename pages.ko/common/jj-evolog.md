# jj evolog

> 변경(Change)이 시간에 따라 어떻게 발전해 왔는지 표시하며, 해당 변경이 이전에 가리켰던 커밋들을 함께 나열.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-evolog>.

- 지정한 리비전의 변경 이력 표시:

`jj evolog {{[-r|--revisions]}} {{revsets}}`

- 변경 이력과 함께 diff 통계 표시:

`jj evolog {{[-r|--revisions]}} {{revsets}} --stat`

- 변경 이력에서 각 변경의 요약 표시:

`jj evolog {{[-r|--revisions]}} {{revsets}} {{[-s|--summary]}}`
