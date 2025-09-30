# pandoc

> 다양한 형식 간에 문서를 변환합니다.
> 더 많은 정보: <https://pandoc.org/MANUAL.html>.

- 파일을 PDF로 변환 (출력 형식은 파일 확장자로 결정됨):

`pandoc {{경로/대상/입력.md}} {{[-o|--output]}} {{경로/대상/출력.pdf}}`

- 적절한 헤더/푸터가 있는 독립 실행형 파일로 변환 (LaTeX, HTML 등):

`pandoc {{경로/대상/입력.md}} {{[-s|--standalone]}} {{[-o|--output]}} {{경로/대상/출력.html}}`

- 형식 감지 및 변환을 수동으로 지정 (파일 이름 확장자를 사용한 자동 형식 감지를 무시하거나 파일 이름 확장자가 전혀 없는 경우):

`pandoc {{-f|-r|--from|--read}} {{docx|...}} {{경로/대상/입력}} {{-t|-w|--to|--write}} {{pdf|...}} {{[-o|--output]}} {{경로/대상/출력}}`

- 지원되는 모든 입력 형식 나열:

`pandoc --list-input-formats`

- 지원되는 모든 출력 형식 나열:

`pandoc --list-output-formats`
