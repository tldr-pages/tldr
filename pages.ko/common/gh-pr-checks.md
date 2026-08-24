# gh pr checks

> GitHub pull request의 CI 검사 상태 확인.
> 더 많은 정보: <https://cli.github.com/manual/gh_pr_checks>.

- 현재 브랜치의 Pull Request 검사 상태 표시:

`gh pr checks`

- 특정 Pull Request의 검사 상태 표시:

`gh pr checks {{PR_번호}}`

- 검사 상태를 완료될 때까지 실시간으로 감시 및 업데이트:

`gh pr checks {{PR_번호}} --watch`

- 필수 검사만 표시:

`gh pr checks {{PR_번호}} --required`
