# crane append

> (선택 사항) 기본 이미지를 기반으로 이미지를 푸시.
> 제공된 tarball의 내용이 포함된 레이어를 추가.
> 더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_append.md>.

- 기본 이미지를 기반으로 하는 이미지 푸시:

`crane append {{[-b|--base]}} {{이미지_이름}}`

- tarball에서 추가된 레이어가 있는 이미지 푸시:

`crane append {{[-f|--new_layer]}} {{레이어_이름1 레이어_이름2 ...}}`

- 새로운 태그가 포함된 레이어가 추가된 이미지 푸시:

`crane append {{[-t|--new_tag]}} {{태그_이름}}`

- 결과 이미지를 새 tarball로 푸시:

`crane append {{[-o|--output]}} {{경로/대상/tarball}}`

- Docker 대신 OCI 미디어 유형의 비어있는 기본 이미지를 사용:

`crane append --oci-empty-base`

- 기본 이미지를 기반으로 결과 이미지에 주석을 달기:

`crane append --set-base-image-annotations`

- 도움말 표시:

`crane append {{[-h|--help]}}`
