# git shortlog

> `git log` 출력을 요약.
> 더 많은 정보: <https://git-scm.com/docs/git-shortlog>.

- 작성자 이름별로 알파벳 순으로 그룹화된 모든 커밋 요약 보기:

`git shortlog`

- 커밋 수에 따라 정렬된 모든 커밋 요약 보기:

`git shortlog {{[-n|--numbered]}}`

- 커미터의 신원(이름과 이메일)별로 그룹화된 모든 커밋 요약 보기:

`git shortlog {{[-c|--committer]}}`

- 마지막 5개의 커밋 요약 보기(즉, 리비전 범위 지정):

`git shortlog HEAD~5..HEAD`

- 현재 브랜치에서 모든 사용자, 이메일 및 커밋 수 요약 보기:

`git shortlog {{[-s|--summary]}} {{[-n|--numbered]}} {{[-e|--email]}}`

- 모든 브랜치에서 모든 사용자, 이메일 및 커밋 수 요약 보기:

`git shortlog {{[-s|--summary]}} {{[-n|--numbered]}} {{[-e|--email]}} --all`
