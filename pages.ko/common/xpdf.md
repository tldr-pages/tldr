# xpdf

> Portable Document Format (PDF) 파일 뷰어.
> 더 많은 정보: <https://www.xpdfreader.com/xpdf-man.html>.

- PDF 파일 열기:

`xpdf {{경로/대상/파일.pdf}}`

- 특정 페이지에서 PDF 파일 열기:

`xpdf {{경로/대상/파일.pdf}} :{{페이지_번호}}`

- 압축된 PDF 파일 열기:

`xpdf {{경로/대상/파일.pdf.tar}}`

- 전체 화면 모드로 PDF 파일 열기:

`xpdf -fullscreen {{경로/대상/파일.pdf}}`

- 초기 줌 비율 지정:

`xpdf -z {{75}}% {{경로/대상/파일.pdf}}`

- 페이지 너비 또는 전체 페이지로 초기 줌 비율 지정:

`xpdf -z {{page|width}} {{경로/대상/파일.pdf}}`
