# markdown2pdf

> markdown을 PDF로 변환.
> 더 많은 정보: <https://github.com/theiskaa/markdown2pdf>.

- Markdown 파일을 PDF로 변환:

`markdown2pdf {{[-p|--path]}} {{경로/대상/입력_파일.md}}`

- Markdown 파일을 지정한 경로의 PDF로 변환:

`markdown2pdf {{[-p|--path]}} {{경로/대상/입력_파일.md}} {{[-o|--output]}} {{경로/대상/출력_파일.pdf}}`

- 문자열 형태의 Markdown 내용을 PDF로 변환:

`markdown2pdf {{[-s|--string]}} {{markdown_문자열}} {{[-o|--output]}} {{경로/대상/출력_파일.pdf}}`

- URL로부터 변환 (해당 URL에 있는 Markdown 파일을 로컬 PDF 파일로 변환):

`markdown2pdf {{[-u|--url]}} {{주소}} {{[-o|--output]}} {{경로/대상/출력_파일.pdf}}`
