# go fmt

> Go 소스 파일을 포맷하고 변경된 파일 이름을 출력합니다.
> 더 많은 정보: <https://pkg.go.dev/cmd/go#hdr-Gofmt__reformat__package_sources>.

- 현재 디렉토리의 Go 소스 파일 포맷:

`go fmt`

- 가져오기 경로(`$GOPATH/src`)에 있는 특정 Go 패키지 포맷:

`go fmt {{경로/대상/패키지}}`

- 현재 디렉토리와 모든 하위 디렉토리의 패키지 포맷 (`...`을 주의하세요):

`go fmt {{./...}}`

- 포맷 명령이 실행될 때 어떤 명령이 실행될지 출력하고 실제로 수정하지 않음:

`go fmt -n`

- 포맷 명령이 실행될 때 실행되는 명령을 출력:

`go fmt -x`
