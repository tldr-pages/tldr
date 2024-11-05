# ebook-convert

> 일반적인 형식 간 전자책을 변환하는 데 사용 가능(예: PDF, EPUB 및 MOBI).
> Calibre 전자책 라이브러리 도구의 일부.
> 더 많은 정보: <https://manual.calibre-ebook.com/generated/en/ebook-convert.html>.

- 전자책을 다른 형식으로 변환:

`ebook-convert {{경로/대상/입력_파일}} {{출력_파일}}`

- Markdown 또는 HTML을 목차, 제목 및 저자가 포함된 전자책으로 변환:

`ebook-convert {{경로/대상/입력_파일}} {{출력_파일}} --level1-toc="//h:h1" --level2-toc="//h:h2" --level3-toc="//h:h3" --title={{title}} --authors={{author}}`
