# jj next

> 작업 복사본(working-copy) 커밋을 자식 리비전으로 이동.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-next>.

- 작업 복사본 커밋을 다음 자식 리비전으로 이동:

`jj next`

- 작업 복사본 커밋을 지정한 개수만큼 앞으로 이동:

`jj next {{offset}}`

- 새 작업 복사본 커밋을 만들지 않고 자식 리비전을 직접 편집:

`jj next {{[-e|--edit]}}`

- 자식 리비전을 직접 편집하지 않고 새 작업 복사본 커밋 생성:

`jj next {{[-n|--no-edit]}}`

- 다음 충돌이 있는 자식 리비전으로 이동:

`jj next --conflict`
