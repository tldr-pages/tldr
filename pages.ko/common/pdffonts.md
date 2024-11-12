# pdffonts

> Portable Document Format (PDF) 파일의 폰트 정보 뷰어.
> 더 많은 정보: <https://www.xpdfreader.com/pdffonts-man.html>.

- PDF 파일의 폰트 정보 출력:

`pdffonts {{경로/대상/파일.pdf}}`

- PDF 파일의 보안 제한을 우회하기 위해 사용자 비밀번호 지정:

`pdffonts -upw {{비밀번호}} {{경로/대상/파일.pdf}}`

- PDF 파일의 보안 제한을 우회하기 위해 소유자 비밀번호 지정:

`pdffonts -opw {{비밀번호}} {{경로/대상/파일.pdf}}`

- PDF 파일이 래스터화될 때 사용될 폰트의 위치에 대한 추가 정보 출력:

`pdffonts -loc {{경로/대상/파일.pdf}}`

- PDF 파일이 PostScript로 변환될 때 사용될 폰트의 위치에 대한 추가 정보 출력:

`pdffonts -locPS {{경로/대상/파일.pdf}}`
