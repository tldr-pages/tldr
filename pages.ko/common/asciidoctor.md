# asciidoctor

> AsciiDoc 파일을 게시 가능한 형식으로 변환하는 프로세서.
> 더 많은 정보: <https://docs.asciidoctor.org>.

- 특정 `.adoc` 파일을 HTML(기본 출력 형식)로 변환:

`asciidoctor {{경로/대상/파일.adoc}}`

- 특정 `.adoc` 파일을 HTML로 변환하고 CSS 스타일시트 연결:

`asciidoctor -a stylesheet={{경로/대상/스타일시트.css}} {{경로/대상/파일.adoc}}`

- 특정 `.adoc` 파일을 포함 가능한 HTML로 변환하고, 본문을 제외한 모든 항목을 제거:

`asciidoctor --embedded {{경로/대상/파일.adoc}}`

- `asciidoctor-pdf` 라이브러리를 사용하여 특정 `.adoc` 파일을 PDF로 변환:

`asciidoctor --backend={{pdf}} --require={{asciidoctor-pdf}} {{경로/대상/파일.adoc}}`
