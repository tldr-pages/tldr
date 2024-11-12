# pdfimages

> PDF에서 이미지를 추출하는 유틸리티.
> 더 많은 정보: <https://manned.org/pdfimages>.

- PDF 파일에서 모든 이미지를 추출하여 PNG로 저장:

`pdfimages -png {{경로/대상/파일.pdf}} {{파일_이름_접두사}}`

- 3페이지부터 5페이지까지의 이미지 추출:

`pdfimages -f {{3}} -l {{5}} {{경로/대상/파일.pdf}} {{파일_이름_접두사}}`

- PDF 파일에서 이미지를 추출하고 출력 파일 이름에 페이지 번호 포함:

`pdfimages -p {{경로/대상/파일.pdf}} {{파일_이름_접두사}}`

- PDF 파일의 모든 이미지에 대한 정보 나열:

`pdfimages -list {{경로/대상/파일.pdf}}`
