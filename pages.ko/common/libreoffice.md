# libreoffice

> 강력하고 무료인 오피스 제품군 LibreOffice의 CLI.
> 더 많은 정보: <https://www.libreoffice.org/>.

- 하나 이상의 파일을 읽기 전용 모드로 열기:

`libreoffice --view {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 하나 이상의 파일 내용 표시:

`libreoffice --cat {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 특정 프린터를 사용하여 파일 인쇄:

`libreoffice --pt {{프린터_이름}} {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 현재 디렉터리의 모든 `.doc` 파일을 PDF로 변환:

`libreoffice --convert-to pdf *.doc`
