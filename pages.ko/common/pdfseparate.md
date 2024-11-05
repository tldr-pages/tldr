# pdfseparate

> 휴대용 문서 형식(PDF) 파일 페이지 추출기.
> 더 많은 정보: <https://manpages.debian.org/latest/poppler-utils/pdfseparate.1.en.html>.

- PDF 파일에서 페이지를 추출하고 각 페이지에 대해 별도의 PDF 파일 생성:

`pdfseparate {{경로/대상/원본_파일_이름.pdf}} {{경로/대상/파일_이름-%d.pdf}}`

- 추출을 위한 시작 페이지 지정:

`pdfseparate -f {{3}} {{경로/대상/원본_파일_이름.pdf}} {{경로/대상/파일_이름-%d.pdf}}`

- 추출을 위한 마지막 페이지 지정:

`pdfseparate -l {{10}} {{경로/대상/원본_파일_이름.pdf}} {{경로/대상/파일_이름-%d.pdf}}`
