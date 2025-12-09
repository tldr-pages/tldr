# gh pr merge

> GitHub 풀 리퀘스트 병합.
> 더 많은 정보: <https://cli.github.com/manual/gh_pr_merge>.

- 현재 브랜치와 연관된 풀 리퀘스트를 대화식으로 병합:

`gh pr merge`

- 지정된 풀 리퀘스트를 대화식으로 병합:

`gh pr merge {{pr_number}}`

- 로컬과 원격 모두에서 브랜치를 삭제하며 풀 리퀘스트 병합:

`gh pr merge --delete-branch`

- 지정된 병합 전략으로 현재 풀 리퀘스트 병합:

`gh pr merge --{{merge|squash|rebase}}`

- 지정된 병합 전략과 커밋 메시지로 현재 풀 리퀘스트 병합:

`gh pr merge --{{merge|squash|rebase}} --subject {{commit_message}}`

- 메시지 본문과 함께 현재 풀 리퀘스트를 하나의 커밋으로 압축하여 병합:

`gh pr merge --squash --body="{{commit_message_body}}"`

- 도움말 표시:

`gh pr merge --help`
