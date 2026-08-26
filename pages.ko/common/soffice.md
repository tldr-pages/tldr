# soffice

> 강력하고 무료인 LibreOffice 제품군을 위한 CLI.
> 더 많은 정보: <https://help.libreoffice.org/latest/en-US/text/shared/guide/pdf_params.html>.

- 하나 이상의 파일을 읽기 전용 모드로 열기:

`soffice --view {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 하나 이상의 파일 내용 표시:

`soffice --cat {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 지정한 프린터를 사용하여 파일 인쇄:

`soffice --pt {{프린터_이름}} {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 현재 디렉터리의 모든 `.doc` 파일을 PDF로 변환:

`soffice --convert-to pdf *.doc`
