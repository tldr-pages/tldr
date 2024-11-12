# daps

> DocBook XML을 HTML 또는 PDF와 같은 출력 형식으로 변환하기 위한 오픈소스 프로그램.
> 더 많은 정보: <https://opensuse.github.io/daps/doc/index.html>.

- DocBook XML 파일이 유효한지 확인:

`daps -d {{경로/대상/파일.xml}} validate`

- DocBook XML 파일을 PDF로 변환:

`daps -d {{경로/대상/파일.xml}} pdf`

- DocBook XML 파일을 단일 HTML file로 뱐환:

`daps -d {{경로/대상/파일.xml}} html --single`

- 도움말 표시:

`daps --help`

- 버전 정보 표시:

`daps --version`
