# git squash

> 여러 커밋을 하나의 커밋으로 합치기.
> `git-extras`의 일부.
> 더 많은 정보: <https://manned.org/git-squash>.

- 특정 브랜치의 모든 커밋을 현재 브랜치에 하나의 커밋으로 합치기:

`git squash {{source_branch}}`

- 현재 브랜치에서 특정 커밋부터 시작하는 모든 커밋을 합치기:

`git squash {{commit}}`

- 최근 `n`개의 커밋을 합치고 메시지와 함께 커밋:

`git squash HEAD~{{n}} "{{메시지}}"`

- 최근 `n`개의 커밋을 합치고 모든 개별 메시지를 연결하여 커밋:

`git squash --squash-msg HEAD~{{n}}`
