# jj prev

> 작업 복사본 커밋을 부모 리비전으로 이동.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-prev>.

- 작업 복사본 커밋을 이전 부모 리비전으로 이동:

`jj prev`

- 작업 복사본 커밋을 지정한 개수만큼 뒤로 이동:

`jj prev {{offset}}`

- 새 작업 복사본 커밋을 만들지 않고, 부모 리비전을 직접 편집:

`jj prev {{[-e|--edit]}}`

- 부모 리비전을 직접 편집하지 않고 새 작업 복사본 커밋 생성:

`jj prev {{[-n|--no-edit]}}`

- 이전 충돌이 있는 부모 리비전으로 이동:

`jj prev --conflict`
