# pdf-parser

> PDF 파일의 기본 요소를 렌더링 없이 식별.
> 더 많은 정보: <https://blog.didierstevens.com/programs/pdf-tools>.

- PDF 파일의 통계 표시:

`pdf-parser --stats {{경로/대상/파일.pdf}}`

- PDF 파일에서 `/Font` 유형의 객체 표시:

`pdf-parser --type={{/Font}} {{경로/대상/파일.pdf}}`

- 간접 객체에서 문자열 검색:

`pdf-parser --search={{검색_문자열}} {{경로/대상/파일.pdf}}`
