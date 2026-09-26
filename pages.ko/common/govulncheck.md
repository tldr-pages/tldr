# govulncheck

> Go 코드에 영향을 미치는 알려진 취약점을 검사하고 보고.
> 참고: `./...`은 Go 도구에서 사용하는 패키지 패턴. 현재 패키지와 현재 디렉터리 아래의 모든 패키지를 재귀적으로 표현.
> 더 많은 정보: <https://pkg.go.dev/golang.org/x/vuln/cmd/govulncheck>.

- 현재 모듈과 해당 의존성의 취약점 검사:

`govulncheck ./...`

- 지정한 패키지의 취약점 검사:

`govulncheck {{경로/대상/패키지}}`

- 소스 코드 대신 Go 바이너리의 취약점 검사:

`govulncheck -mode binary {{경로/대상/바이너리}}`

- Go 바이너리에서 빌드 정보와 빌드 의존성 추출:

`govulncheck -mode extract {{경로/대상/바이너리}}`

- 테스트 파일도 포함하여 취약점 검사:

`govulncheck -test ./...`

- 지정한 형식으로 검사 결과 출력:

`govulncheck -format {{text|json|sarif|openvex}} ./...`

- 각 취약한 심볼에 도달하는 호출 스택 표시:

`govulncheck -show traces ./...`
