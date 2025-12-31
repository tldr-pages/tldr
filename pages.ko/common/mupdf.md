# mupdf

> 경량 PDF, XPS 및 전자책 뷰어.
> 더 많은 정보: <https://mupdf.readthedocs.io/en/latest/tools/mupdf-gl.html>.

- 첫 페이지에서 PDF 열기:

`mupdf {{경로/대상/파일}}`

- 3페이지에서 PDF 열기:

`mupdf {{경로/대상/파일}} {{3}}`

- 비밀번호로 보호된 PDF 열기:

`mupdf -p {{비밀번호}} {{경로/대상/파일}}`

- 초기 확대 수준(72 DPI)으로 PDF 열기:

`mupdf -r {{72}} {{경로/대상/파일}}`

- 색상이 반전된 PDF 열기:

`mupdf -I {{경로/대상/파일}}`

- 빨간색 #FF0000 틴트가 적용된 PDF 열기 (16진수 색상 구문 RRGGBB):

`mupdf -C {{FF0000}}`

- 안티앨리어싱 없이 PDF 열기 (0 = 끔, 8 = 최고):

`mupdf -A {{0}}`
