# gh pr create

> GitHub 풀 리퀘스트 관리.
> 더 많은 정보: <https://cli.github.com/manual/gh_pr_create>.

- 대화형으로 풀 리퀘스트 생성:

`gh pr create`

- 현재 브랜치의 커밋 메시지에서 제목과 설명을 결정하여 풀 리퀘스트 생성:

`gh pr create --fill`

- 드래프트 풀 리퀘스트 생성:

`gh pr create --draft`

- 베이스 브랜치, 제목 및 설명을 지정하여 풀 리퀘스트 생성:

`gh pr create --base {{베이스_브랜치}} --title "{{제목}}" --body "{{본문}}"`

- 기본 웹 브라우저에서 풀 리퀘스트 열기 시작:

`gh pr create --web`
