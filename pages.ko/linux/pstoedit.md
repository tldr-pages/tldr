# pstoedit

> PDF 파일을 다양한 이미지 형식으로 변환합니다.
> 더 많은 정보: <http://www.pstoedit.net>.

- PDF 페이지를 PNG 또는 JPEG 형식으로 변환:

`pstoedit -page {{페이지_번호}} -f magick {{경로/대상/파일.pdf}} {{페이지.png|페이지.jpg]}}`

- 여러 PDF 페이지를 번호가 매겨진 이미지로 변환:

`pstoedit -f magick {{경로/대상/파일}} {{페이지%d.png|페이지%d.jpg}}`
