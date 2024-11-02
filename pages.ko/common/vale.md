# vale

> Markdown 및 AsciiDoc과 같은 여러 마크업 형식을 지원하는 확장 가능한 스타일 검사기.
> 더 많은 정보: <https://vale.sh>.

- 파일의 스타일 검사:

`vale {{경로/대상/파일}}`

- 지정된 설정 파일을 사용하여 파일의 스타일 검사:

`vale --config='{{경로/대상/.vale.ini}}' {{경로/대상/파일}}`

- 결과를 JSON 형식으로 출력:

`vale --output=JSON {{경로/대상/파일}}`

- 특정 심각도 이상의 스타일 문제 검사:

`vale --minAlertLevel={{suggestion|warning|error}} {{경로/대상/파일}}`

- `stdin`에서 스타일 검사, 마크업 형식 지정:

`cat {{파일.md}} | vale --ext=.md`

- 현재 설정 나열:

`vale ls-config`
