# gh pr comment

> GitHub Pull Request에 댓글 추가.
> 더 많은 정보: <https://cli.github.com/manual/gh_pr_comment>.

- 현재 브랜치의 Pull Request에 댓글 작성:

`gh pr comment {{[-b|--body]}} "{{LGTM}}"`

- 특정 Pull Request에 댓글 작성:

`gh pr comment {{123}} {{[-b|--body]}} "{{Thanks!}}"`

- 파일 내용을 사용해 댓글 작성:

`gh pr comment {{123}} {{[-F|--body-file]}} {{경로/대상/파일.txt}}`

- 여러 줄 댓글 작성을 위한 편집기 열기:

`gh pr comment {{123}}`
