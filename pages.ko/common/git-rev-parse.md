# git rev-parse

> 리비전에 관련된 메타데이터를 표시.
> 더 많은 정보: <https://git-scm.com/docs/git-rev-parse>.

- 브랜치의 커밋 해시 가져오기:

`git rev-parse {{브랜치_이름}}`

- 현재 브랜치 이름 가져오기:

`git rev-parse --abbrev-ref {{HEAD}}`

- 루트 디렉토리의 절대 경로 가져오기:

`git rev-parse --show-toplevel`
