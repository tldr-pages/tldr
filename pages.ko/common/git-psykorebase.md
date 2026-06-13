# git psykorebase

> 병합 커밋과 단 한 번의 충돌 처리를 사용하여 브랜치를 다른 브랜치 위에 리베이스합니다.
> `git-extras`의 일부입니다.
> 더 많은 정보: <https://manned.org/git-psykorebase>.

- 병합 커밋과 단 한 번의 충돌 처리를 사용하여 현재 브랜치를 다른 브랜치 위에 리베이스:

`git psykorebase {{업스트림_브랜치}}`

- 충돌이 해결된 후 계속 진행:

`git psykorebase --continue`

- 리베이스할 브랜치 지정:

`git psykorebase {{업스트림_브랜치}} {{대상_브랜치}}`
