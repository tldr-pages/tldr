# gofmt

> Go 소스 코드를 포맷합니다.
> 더 많은 정보: <https://pkg.go.dev/cmd/gofmt>.

- 파일을 포맷하고 결과를 콘솔에 표시:

`gofmt {{source.go}}`

- 파일을 포맷하여 원본 파일을 덮어쓰기:

`gofmt -w {{source.go}}`

- 파일을 포맷하고 코드를 단순화한 후 원본 파일을 덮어쓰기:

`gofmt -s -w {{source.go}}`

- 모든 오류(불필요한 오류 포함)를 출력:

`gofmt -e {{source.go}}`
