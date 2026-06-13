# pdfinfo

> Portable Document Format (PDF) 파일 정보 뷰어.
> 더 많은 정보: <https://www.xpdfreader.com/pdfinfo-man.html>.

- PDF 파일 정보 출력:

`pdfinfo {{경로/대상/파일.pdf}}`

- 보안 제한을 우회하기 위해 PDF 파일의 사용자 비밀번호 지정:

`pdfinfo -upw {{비밀번호}} {{경로/대상/파일.pdf}}`

- 보안 제한을 우회하기 위해 PDF 파일의 소유자 비밀번호 지정:

`pdfinfo -opw {{비밀번호}} {{경로/대상/파일.pdf}}`
