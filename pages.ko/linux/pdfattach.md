# pdfattach

> 기존 PDF 파일에 새 첨부 파일(내장 파일)을 추가.
> 같이 보기: `pdfdetach`, `pdfimages`, `pdfinfo`.
> 더 많은 정보: <https://manned.org/pdfattach>.

- 기존 PDF 파일에 새 첨부 파일 추가:

`pdfattach {{경로/대상/input.pdf}} {{경로/대상/첨부할_파일}} {{경로/대상/output.pdf}}`

- 같은 이름의 첨부 파일이 존재할 경우 교체:

`pdfattach -replace {{경로/대상/input.pdf}} {{경로/대상/첨부할_파일}} {{경로/대상/output.pdf}}`

- 도움말 표시:

`pdfattach -h`

- 버전 표시:

`pdfattach -v`
