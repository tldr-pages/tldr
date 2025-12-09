# glab mr create

> GitLab 병합 요청을 관리.
> 더 많은 정보: <https://gitlab.com/gitlab-org/cli/-/blob/main/docs/source/mr/create.md>.

- 대화형으로 병합 요청을 생성:

`glab mr create`

- 현재 브랜치의 커밋 메시지에서 제목과 설명을 결정하여 병합 요청을 생성:

`glab mr create {{[-f|--fill]}}`

- 초안 병합 요청을 생성:

`glab mr create --draft`

- 대상 브랜치, 제목 및 설명을 지정하는 병합 요청을 생성:

`glab mr create {{[-b|--target-branch]}} {{대상_브랜치}} {{[-t|--title]}} "{{제목}}" {{[-d|--description]}} "{{설명}}"`

- 기본 웹 브라우저에서 병합 요청 열기를 시작:

`glab mr create {{[-w|--web]}}`
