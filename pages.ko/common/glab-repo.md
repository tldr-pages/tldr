# glab repo

> GitLab 레포지토리 작업.
> 더 많은 정보: <https://gitlab.com/gitlab-org/cli/-/blob/main/docs/source/repo/index.md>.

- 새로운 저장소를 생성 (저장소 이름이 설정되지 않은 경우, 기본 이름은 현재 디렉터리의 이름이 됨):

`glab repo create {{이름}}`

- 레포지토리 복제:

`glab repo clone {{소유자}}/{{레포지토리}}`

- 레포지토리 포크 및 복제:

`glab repo fork {{소유자}}/{{레포지토리}} {{[-c|--clone]}}`

- 기본 웹 브라우저에서 레포지토리 보기:

`glab repo view {{소유자}}/{{레포지토리}} {{[-w|--web]}}`

- GitLab 인스턴스에서 일부 레포지토리를 검색:

`glab repo search {{[-s|--search]}} {{검색_문자열}}`
