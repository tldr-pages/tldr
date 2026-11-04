# jj converge

> 분기된 변경 사항을 하나로 통합.
> 지정한 변경에 대해 두 개 이상의 표시되는 리비전을 하나의 리비전으로 대체하여 분기를 해결.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-converge>.

- 기본 검색 범위에서 분기된 리비전 통합 (`revsets.converge`에 설정됨):

`jj converge`

- 지정한 검색 범위에서 분기된 리비전 통합:

`jj converge {{[-r|--revision]}} {{revset}}`

- 대화형 입력 없이 분기 해결:

`jj converge --no-interactive`
