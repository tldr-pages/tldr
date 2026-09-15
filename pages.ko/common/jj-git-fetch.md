# jj git fetch

> Git 원격 저장소에서 객체와 참조를 다운로드하여 가져옴.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-git-fetch>.

- 기본 원격 저장소에서 최신 변경 사항 가져오기:

`jj git fetch`

- 지정한 원격 저장소에서 최신 변경 사항 가져오기:

`jj git fetch --remote {{원격_저장소}}`

- 지정한 브랜치의 최신 변경 사항만 가져오기:

`jj git fetch {{[-b|--branch]}} {{브랜치}}`

- 모든 원격 저장소에서 최신 변경 사항 가져오기:

`jj git fetch --all-remote`
