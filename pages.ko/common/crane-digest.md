# crane digest

> 이미지의 다이제스트를 가져옴.
> 더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_digest.md>.

- 이미지의 다이제스트를 가져옴:

`crane digest {{이미지_이름}}`

- 다이제스트로 전체 이미지 참조를 출력:

`crane digest {{이미지_이름}} --full-ref`

- 이미지가 포함된 tarball의 경로를 지정:

`crane digest {{이미지_이름}} --tarball {{경로/대상/tarball}}`

- 도움말 표시:

`crane digest {{[-h|--help]}}`
