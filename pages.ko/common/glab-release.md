# glab release

> GitLab 배포 관맄.
> 더 많은 정보: <https://gitlab.com/gitlab-org/cli/-/blob/main/docs/source/release/index.md>.

- Gitlab 저장소의 릴리스 목록은 30개 항목으로 제한됨:

`glab release list`

- 특정 릴리스에 대한 정보 표시:

`glab release view {{태그}}`

- 새로운 배포 생성:

`glab release create {{태그}}`

- 특정 배포 삭제:

`glab release delete {{태그}}`

- 특정 릴리스에서 리소스 다운로드:

`glab release download {{태그}}`

- 특정 릴리스에 리소스 업로드:

`glab release upload {{태그}} {{경로/대상/파일1 경로/대상/파일2 ...}}`
