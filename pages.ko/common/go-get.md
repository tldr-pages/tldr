# go get

> 의존성 패키지를 추가하거나 레거시 GOPATH 모드에서 패키지를 다운로드.
> 더 많은 정보: <https://pkg.go.dev/cmd/go#hdr-Add_dependencies_to_current_module_and_install_them>.

- 모듈 모드에서 `go.mod`에 지정된 패키지를 추가하거나 GOPATH 모드에서 패키지 설치:

`go get {{example.com/pkg}}`

- 모듈 인식 모드에서 지정된 버전으로 패키지 수정:

`go get {{example.com/pkg}}@{{v1.2.3}}`

- 지정된 패키지 제거:

`go get {{example.com/pkg}}@{{none}}`
