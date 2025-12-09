# gh release

> GitHub 릴리스 관리.
> 더 많은 정보: <https://cli.github.com/manual/gh_release>.

- GitHub 저장소의 릴리스 목록 표시, 최대 30개 항목으로 제한:

`gh release list`

- 특정 릴리스에 대한 정보 표시:

`gh release view {{태그}}`

- 새 릴리스 생성:

`gh release create {{태그}}`

- 특정 릴리스 삭제:

`gh release delete {{태그}}`

- 특정 릴리스에서 자산 다운로드:

`gh release download {{태그}}`

- 특정 릴리스에 자산 업로드:

`gh release upload {{태그}} {{경로/대상/파일1 경로/대상/파일2 ...}}`
