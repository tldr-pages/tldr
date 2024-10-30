# ocrmypdf

> 스캔한 PDF나 텍스트 이미지에서 검색 가능한 PDF 또는 PDF/A를 생성.
> 더 많은 정보: <https://ocrmypdf.readthedocs.io/en/latest/cookbook.html>.

- 스캔한 PDF 또는 이미지 파일에서 새로운 검색 가능한 PDF/A 파일 생성:

`ocrmypdf {{경로/대상/입력_파일}} {{경로/대상/출력.pdf}}`

- 스캔한 PDF 파일을 검색 가능한 PDF 파일로 교체:

`ocrmypdf {{경로/대상/파일.pdf}} {{경로/대상/파일.pdf}}`

- 텍스트가 이미 포함된 혼합 형식 입력 PDF 파일의 페이지 건너뛰기:

`ocrmypdf --skip-text {{경로/대상/입력.pdf}} {{경로/대상/출력.pdf}}`

- 불량 스캔의 페이지를 정리하고, 기울임 보정하고, 회전:

`ocrmypdf --clean --deskew --rotate-pages {{경로/대상/입력_파일}} {{경로/대상/출력.pdf}}`

- 검색 가능한 PDF 파일의 메타데이터 설정:

`ocrmypdf --title "{{제목}}" --author "{{저자}}" --subject "{{주제}}" --keywords "{{키워드; 키 구문; ...}}" {{경로/대상/입력_파일}} {{경로/대상/출력.pdf}}`

- 도움말 표시:

`ocrmypdf --help`
