# go list

> 패키지 또는 모듈 나열.
> 더 많은 정보: <https://pkg.go.dev/cmd/go#hdr-List_packages_or_modules>.

- 패키지 나열:

`go list ./...`

- 표준 패키지 나열:

`go list std`

- JSON 형식으로 패키지 나열:

`go list -json time net/http`

- 모듈 종속성과 이용 가능한 업데이트 나열:

`go list -m -u all`
