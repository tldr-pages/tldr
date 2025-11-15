# crane export

> 컨테이너 이미지의 파일 시스템을 tarball로 내보냄.
> 더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_digest.md>.

- `stdout`에 tarball을 작성 :

`crane export {{이미지_이름}} -`

- 파일에 tarball 쓰기:

`crane export {{이미지_이름}} {{경로/대상/tarball}}`

- `stdin`에서 이미지 읽기:

`crane export - {{경로/대상/파일이름}}`
