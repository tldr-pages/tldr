# crane rebase

> 이미지를 새로운 기본 이미지로 rebase.
> 더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_rebase.md>.

- 이미지 rebase:

`crane rebase`

- 새로운 기본 이미지 삽입:

`crane rebase --new_base {{이미지_이름}}`

- 오래된 이미지 제거:

`crane rebase --old_base {{이미지_이름}}`

- rebase된 이미지에 적용할 태그 추가:

`crane rebase {{[-t|--tag]}} {{태그_이름}}`

- 도움말 표시:

`crane rebase {{[-h|--help]}}`
