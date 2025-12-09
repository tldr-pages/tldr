# godoc

> Go 패키지에 대한 문서를 확인.
> 더 많은 정보: <https://pkg.go.dev/golang.org/x/tools/cmd/godoc>.

- 특정 패키지에 대한 도움말 표시:

`godoc {{fmt}}`

- "fmt" 패키지의 "Printf" 함수에 대한 도움말 표시:

`godoc {{fmt}} {{Printf}}`

- 포트 6060에서 웹 서버로 문서 제공:

`godoc -http=:{{6060}}`

- 인덱스 파일을 생성:

`godoc -write_index -index_files={{경로/대상/파일}}`

- 주어진 색인 파일을 사용하여 문서를 검색:

`godoc -http=:{{6060}} -index -index_files={{경로/대상/파일}}`
