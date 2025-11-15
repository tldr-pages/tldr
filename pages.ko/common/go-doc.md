# go doc

> 패키지나 심볼에 대한 문서 보기.
> 더 많은 정보: <https://pkg.go.dev/cmd/go#hdr-Show_documentation_for_package_or_symbol>.

- 현재 패키지에 대한 문서 보기:

`go doc`

- 패키지 문서 및 내보내진 기호 보기:

`go doc {{encoding/json}}`

- 기호의 문서도 함께 보기:

`go doc -all {{encoding/json}}`

- 소스도 함께 보기:

`go doc -all -src {{encoding/json}}`

- 특정 기호 보기:

`go doc -all -src {{encoding/json.Number}}`
