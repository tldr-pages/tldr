# git summary

> Git 저장소에 대한 정보를 표시.
> `git-extras`의 일부.
> 더 많은 정보: <https://manned.org/git-summary>.

- Git 저장소에 대한 정보 표시:

`git summary`

- 특정 커밋 이후의 Git 저장소에 대한 정보 표시:

`git summary {{커밋|브랜치_명|태그_명}}`

- 서로 다른 이메일을 사용하는 커미터를 저자별 통계로 합산하여 Git 저장소에 대한 정보 표시:

`git summary --dedup-by-email`

- 각 기여자가 수정한 줄 수를 표시하여 Git 저장소에 대한 정보 표시:

`git summary --line`
