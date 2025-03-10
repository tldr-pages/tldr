# crane pull

> 참조를 통해 원격 이미지를 가져오고 해당 콘텐츠를 로컬에 저장.
> 더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_pull.md>.

- 원격 이미지 가져오기:

`crane pull {{이미지_이름}} {{경로/대상/tarball}}`

- --format=oci와 함께 사용할 때 주석으로 가져오는 데 사용되는 이미지 참조를 유지:

`crane pull {{이미지_이름}} {{경로/대상/tarball}} --annotate-ref`

- 캐시 이미지 레이어 경로:

`crane pull {{이미지_이름}} {{경로/대상/tarball}} {{[-c|--cache_path]}} {{경로/대상/캐시}}`

- 이미지를 저장할 형식 지정 (기본값 'tarball'):

`crane pull {{이미지_이름}} {{경로/대상/tarball}} {{-format}} {{포맷_이름}}`

- 도움말 표시:

`crane pull {{[-h|--help]}}`
