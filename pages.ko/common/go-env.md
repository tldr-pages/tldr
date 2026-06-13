# go env

> Go 툴체인이 사용하는 환경 변수를 관리합니다.
> 더 많은 정보: <https://pkg.go.dev/cmd/go#hdr-Print_Go_environment_information>.

- 모든 환경 변수 표시:

`go env`

- 특정 환경 변수 표시:

`go env {{GOPATH}}`

- 환경 변수를 특정 값으로 설정:

`go env -w {{GOBIN}}={{경로/대상/폴더}}`

- 환경 변수의 값을 재설정:

`go env -u {{GOBIN}}`
