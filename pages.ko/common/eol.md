# eol

> 여러 제품의 수명 종료 날짜(EoL)를 표시.
> 더 많은 정보: <https://github.com/hugovk/norwegianblue>.

- 사용 가능한 모든 제품의 목록을 나열:

`eol`

- 하나 이상의 제품에 대한 EoL을 가져옴:

`eol {{제품1 제품2 ...}}`

- 제품 웹페이지 열기:

`eol {{제품}} --web`

- 특정 형식으로 하나 이상의 제품에 대한 EoL을 가져옴노:

`eol {{제품1 제품2 ...}} --format {{html|json|md|markdown|pretty|rst|csv|tsv|yaml}}`

- 하나 이상의 제품에 대한 EoL을 단일 마크다운 파일로 가져옴:

`eol {{제품1 제품2 ...}} --format {{마크다운}} > {{eol_보고서.md}}`

- 도움말 표시:

`eol --help`
