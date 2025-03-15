# crane push

> 로컬 이미지 콘텐츠를 원격 레지스트리로 푸시.
> 더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_push.md>.

- 로컬 이미지 콘텐츠를 원격 레지스트리로 푸시:

`crane push {{경로/대상/tarball}} {{이미지_이름}}`

- 게시된 이미지 참조 목록이 있는 파일 경로:

`crane push {{경로/대상/tarball}} {{이미지_이름}} --image-refs {{경로/대상/파일이름}}`

- 이미지 모음을 단일 인덱스로 푸시 (경로에 여러 이미지가 있는 경우 필수):

`crane push {{경로/대상/tarball}} {{이미지_이름}} --index`

- 도움말 표시:

`crane push {{[-h|--help]}}`
