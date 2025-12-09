# gs

> GhostScript는 PDF 및 PostScript 인터프리터입니다.
> 더 많은 정보: <https://manned.org/gs>.

- 파일 보기:

`gs -dQUIET -dBATCH {{파일.pdf}}`

- e-book 기기에서 읽을 수 있도록 PDF 파일 크기를 150 dpi 이미지로 줄이기:

`gs -dNOPAUSE -dQUIET -dBATCH -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -sOutputFile={{출력.pdf}} {{입력.pdf}}`

- PDF 파일의 페이지 1부터 3까지를 150 dpi 해상도의 이미지로 변환:

`gs -dQUIET -dBATCH -dNOPAUSE -sDEVICE=jpeg -r150 -dFirstPage={{1}} -dLastPage={{3}} -sOutputFile={{출력_%d.jpg}} {{입력.pdf}}`

- PDF 파일에서 페이지 추출:

`gs -dQUIET -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile={{출력.pdf}} {{입력.pdf}}`

- PDF 파일 병합:

`gs -dQUIET -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile={{출력.pdf}} {{입력1.pdf}} {{입력2.pdf}}`

- PostScript 파일을 PDF 파일로 변환:

`gs -dQUIET -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile={{출력.pdf}} {{입력.ps}}`
