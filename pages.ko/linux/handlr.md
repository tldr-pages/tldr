# handlr

> 기본 애플리케이션을 관리합니다.
> 더 많은 정보: <https://github.com/chmln/handlr#usage>.

- 기본 애플리케이션에서 URL 열기:

`handlr open {{https://example.com}}`

- 기본 PDF 뷰어에서 PDF 열기:

`handlr open {{경로/대상/파일.pdf}}`

- PNG 파일의 기본 애플리케이션으로 `imv` 설정:

`handlr set {{.png}} {{imv.desktop}}`

- 모든 오디오 파일의 기본 애플리케이션으로 MPV 설정:

`handlr set {{'audio/*'}} {{mpv.desktop}}`

- 모든 기본 앱 나열:

`handlr list`

- PNG 파일의 기본 애플리케이션 출력:

`handlr get {{.png}}`
