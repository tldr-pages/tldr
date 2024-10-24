# pdftohtml

> PDF 파일을 HTML, XML 및 PNG 이미지로 변환.
> 더 많은 정보: <https://manned.org/pdftohtml>.

- PDF 파일을 HTML 파일로 변환:

`pdftohtml {{경로/대상/파일.pdf}} {{경로/대상/출력_파일.html}}`

- PDF 파일에서 이미지를 무시:

`pdftohtml -i {{경로/대상/파일.pdf}} {{경로/대상/출력_파일.html}}`

- 모든 PDF 페이지를 포함하는 단일 HTML 파일 생성:

`pdftohtml -s {{경로/대상/파일.pdf}} {{경로/대상/출력_파일.html}}`

- PDF 파일을 XML 파일로 변환:

`pdftohtml -xml {{경로/대상/파일.pdf}} {{경로/대상/출력_파일.xml}}`
