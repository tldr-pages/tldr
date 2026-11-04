# jj resolve

> 외부 병합 도구를 사용하여 충돌이 발생한 파일을 해결.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-resolve>.

- 모든 충돌 해결:

`jj resolve`

- 모든 충돌 목록 표시:

`jj resolve {{[-l|--list]}}`

- 지정한 리비전의 충돌 해결:

`jj resolve {{[-r|--revision]}} {{revset}}`

- 지정한 파일의 충돌 해결:

`jj resolve {{파일1 파일2 ...}}`

- 들어오는 버전을 선택하여 충돌 해결:

`jj resolve --tool :theirs`

- 현재 버전을 선택하여 충돌 해결:

`jj resolve --tool :ours`
