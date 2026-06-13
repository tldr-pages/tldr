# img2pdf

> 래스터 이미지를 무손실로 PDF 파일로 변환.
> 지원되는 이미지 포맷으로는 GIF, JPEG, JPEG2000, PNG, GIF, TIFF 등이 있습니다.
> 더 많은 정보: <https://gitlab.mister-muffin.de/josch/img2pdf>.

- 하나 이상의 이미지를 각각의 페이지에 넣어 단일 PDF로 변환:

`img2pdf {{경로/대상/이미지1.확장자 경로/대상/이미지2.확장자 ...}} --output {{경로/대상/파일.pdf}}`

- 다중 프레임 이미지의 첫 프레임만 PDF로 변환:

`img2pdf {{경로/대상/파일.gif}} --first-frame-only --output {{경로/대상/파일.pdf}}`

- 이미지를 자동으로 방향 설정하고, 가로 모드의 특정 페이지 크기를 사용하며, 가로 및 세로로 특정 크기의 테두리를 설정:

`img2pdf {{경로/대상/이미지.확장자}} --auto-orient --pagesize {{A4^T}} --border {{2cm}}:{{5.1cm}} --output {{경로/대상/파일.pdf}}`

- 페이지의 특정 크기 내에 지정된 치수로만 큰 이미지를 축소:

`img2pdf {{경로/대상/이미지.확장자}} --pagesize {{30cm}}x{{20cm}} --imgsize {{10cm}}x{{15cm}} --fit {{shrink}} --output {{경로/대상/파일.pdf}}`

- 이미지를 PDF로 변환하고, 결과 파일에 메타데이터 지정:

`img2pdf {{경로/대상/이미지.확장자}} --title {{제목}} --author {{저자}} --creationdate {{1970-01-31}} --keywords {{키워드1 키워드2}} --subject {{주제}} --output {{경로/대상/파일.pdf}}`
