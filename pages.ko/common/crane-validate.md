# crane validate

> 이미지의 형식이 올바른지 확인.
> 더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_validate.md>.

- 이미지 유효성 검사:

`crane validate`

- 레이어 다운로드/다이제스트 건너뛰기:

`crane validate --fast`

- 유효성을 검사할 원격 이미지의 이름:

`crane validate --remote {{이미지_이름}}`

- 유효성을 검사할 tarball 경로:

`crane validate --tarball {{경로/대상/tarball}}`

- 도움말 표시:

`crane validate {{[-h|--help]}}`
