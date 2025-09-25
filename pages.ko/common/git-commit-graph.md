# git commit-graph

> Git commit-graph 파일을 작성하고 검증합니다.
> 더 많은 정보: <https://git-scm.com/docs/git-commit-graph>.

- 저장소의 로컬 `.git` 디렉토리에 있는 모든 커밋들에 대한 commit-graph 파일 작성:

`git commit-graph write`

- 모든 브랜치와 태그에서 접근 가능한 커밋들을 포함하는 commit-graph 파일 작성:

`git show-ref {{[-s|--hash]}} | git commit-graph write --stdin-commits`

- 현재 commit-graph 파일의 모든 커밋과 현재 `HEAD`에서 접근 가능한 커밋들을 포함하는 업데이트된 commit-graph 파일 작성:

`git rev-parse {{HEAD}} | git commit-graph write --stdin-commits --append`
