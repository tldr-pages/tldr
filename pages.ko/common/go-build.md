# go build

> Go 소스 컴파일.
> 더 많은 정보: <https://pkg.go.dev/cmd/go#hdr-Compile_packages_and_dependencies>.

- 'package main' 파일 컴파일 (출력은 확장자가 없는 파일 이름):

`go build {{경로/대상/main.go}}`

- 출력 파일 이름을 지정하여 컴파일:

`go build -o {{경로/대상/바이너리}} {{경로/대상/소스.go}}`

- 패키지 컴파일:

`go build -o {{경로/대상/바이너리}} {{경로/대상/패키지}}`

- 데이터 경쟁 감지를 활성화하여 메인 패키지를 실행 파일로 컴파일:

`go build -race -o {{경로/대상/실행_파일}} {{경로/대상/메인/패키지}}`
