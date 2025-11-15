# zek

> XML에서 Go 구조체 생성.
> 더 많은 정보: <https://github.com/miku/zek#usage>.

- `stdin`에서 주어진 XML로부터 Go 구조체를 생성하고 결과를 `stdout`에 출력:

`cat {{경로/대상/입력.xml}} | zek`

- `stdin`에서 주어진 XML로부터 Go 구조체를 생성하고 결과를 파일로 저장:

`curl -s {{https://url/대상/xml}} | zek -o {{경로/대상/출력.go}}`

- `stdin`에서 주어진 XML로부터 예제 Go 프로그램을 생성하고 결과를 파일로 저장:

`cat {{경로/대상/입력.xml}} | zek -p -o {{경로/대상/출력.go}}`
