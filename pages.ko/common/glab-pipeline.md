# glab pipeline

> GitLab CI/CD 파이프라인을 나열, 보고, 실행.
> 더 많은 정보: <https://gitlab.com/gitlab-org/cli/-/blob/main/docs/source/index.md>.

- 현재 브랜치에서 실행 중인 파이프라인을 보기:

`glab pipeline status`

- 특정 분기에서 실행 중인 파이프라인을 보기:

`glab pipeline status --branch {{브랜치_이름}}`

- 파이프라인 목록을 가져옴:

`glab pipeline list`

- 현재 브랜치에서 수동 파이프라인을 실행:

`glab pipeline run`

- 특정 브랜치에서 수동 파이프라인을 실행:

`glab pipeline run --branch {{브랜치_이름}}`
