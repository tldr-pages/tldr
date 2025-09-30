# pdfdetach

> PDF 파일에서 첨부 파일(내장 파일)을 나열하거나 추출.
> 같이 보기: `pdfattach`, `pdfimages`, `pdfinfo`.
> 더 많은 정보: <https://manned.org/pdfdetach>.

- 특정 텍스트 인코딩으로 파일의 모든 첨부 파일 나열:

`pdfdetach list -enc {{UTF-8}} {{경로/대상/입력.pdf}}`

- 번호를 지정하여 특정 내장 파일 저장:

`pdfdetach -save {{번호}} {{경로/대상/입력.pdf}}`

- 이름을 지정하여 특정 내장 파일 저장:

`pdfdetach -savefile {{이름}} {{경로/대상/입력.pdf}}`

- 사용자 지정 출력 파일 이름으로 내장 파일 저장:

`pdfdetach -save {{번호}} -o {{경로/대상/출력}} {{경로/대상/입력.pdf}}`

- 소유자/사용자 암호로 보호된 파일에서 첨부 파일 저장:

`pdfdetach -save {{번호}} {{-opw|-upw}} {{암호}} {{경로/대상/입력.pdf}}`
