# glab mr merge

> GitLab 병합 요청을 관리.
> 더 많은 정보: <https://gitlab.com/gitlab-org/cli/-/blob/main/docs/source/mr/merge.md>.

- 현재 브랜치와 관련된 병합 요청을 대화식으로 병합:

`glab mr merge`

- 지정된 병합 요청을 대화식으로 병합:

`glab mr merge {{mr_번호}}`

- 로컬과 원격 모두에서 브랜치를 제거하여 병합 요청을 병합:

`glab mr merge {{[-d|--remove-source-branch]}}`

- 현재 병합 요청을 메시지 본문과 함께 하나의 커밋으로 스쿼시하고 병합:

`glab mr merge {{[-s|--squash]}} {{[-m|--message]}} "{{커밋_메시지_본체}}"`

- 도움말 표시:

`glab mr merge --help`
