# goimports

> Go 언어의 import 줄을 업데이트하여 누락된 항목을 추가하고 참조되지 않은 항목을 제거합니다.
> 더 많은 정보: <https://pkg.go.dev/golang.org/x/tools/cmd/goimports>.

- 완료된 import 소스 파일 표시:

`goimports {{경로/대상/파일.go}}`

- 결과를 `stdout` 대신 소스 파일에 다시 작성:

`goimports -w {{경로/대상/파일.go}}`

- 차이점을 표시하고 결과를 소스 파일에 다시 작성:

`goimports -w -d {{경로/대상/파일.go}}`

- 3rd-party 패키지 이후에 import 접두사 문자열 설정 (쉼표로 구분된 목록):

`goimports -local {{경로/대상/패키지1,경로/대상/패키지2,...}} {{경로/대상/파일.go}}`
