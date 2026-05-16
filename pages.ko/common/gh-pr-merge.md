# gh pr merge

> GitHub Pull Request 병합.
> 더 많은 정보: <https://cli.github.com/manual/gh_pr_merge>.

- 현재 브랜치와 연결된 Pull Request를 대화형으로 병합:

`gh pr merge`

- 현재 브랜치를 지정한 Pull Request에 merge 방식으로 병합:

`gh pr merge {{PR_번호}} {{[-m|--merge]}}`

- Pull Request를 squash 병합하고, 브랜치 삭제:

`gh pr merge {{PR_번호}} {{[-sd|--squash --delete-branch]}}`

- rebase 방식으로 병합:

`gh pr merge {{PR_번호}} {{[-r|--rebase]}}`

- 자동 병합(auto-merge) 활성화 (squash 방식):

`gh pr merge {{PR_번호}} --auto {{[-s|--squash]}}`

- 관리자 권한으로 병합 (허용된 경우):

`gh pr merge {{PR_번호}} --admin`
