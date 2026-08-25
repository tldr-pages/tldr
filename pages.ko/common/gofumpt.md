# gofumpt

> Go 파일을 엄격한 규칙으로 포맷하는 도구.
> 관련 항목: `gofmt`.
> 더 많은 정보: <https://github.com/mvdan/gofumpt#gofumpt>.

- Go 파일 포맷 적용:

`gofumpt -w {{경로/대상/디렉터리}}`

- `gofumpt` 포맷과 다른 파일 목록([l]ist) 표시:

`gofumpt -l {{경로/대상/디렉터리}}`

- 모든 오류([e]rrors) 보고:

`gofumpt -e {{경로/대상/디렉터리}}`

- 변경 사항([d]iffs) 표시:

`gofumpt -d {{경로/대상/디렉터리}}`

- 더욱 엄격한 규칙으로 Go 파일 포맷:

`gofumpt -extra {{경로/대상/디렉터리}}`

- 더욱 엄격한 규칙 기준으로 변경 사항([d]iffs) 표시:

`gofumpt -extra -d {{경로/대상/디렉터리}}`

- 도움말 표시:

`gofumpt {{[-h|--help]}}`
