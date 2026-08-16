# sqlfluff

> 여러 SQL 방언을 지원하며 SQL 파일을 린트하고 자동으로 포맷.
> 더 많은 정보: <https://docs.sqlfluff.com/en/stable/reference/cli.html>.

- 지정한 SQL 방언을 사용하여 SQL 파일 또는 디렉터리 린트:

`sqlfluff lint {{[-d|--dialect]}} {{방언}} {{경로/대상/파일_또는_디렉터리}}`

- 지정한 SQL 방언을 사용하여 SQL 파일 또는 디렉터리 자동 포맷:

`sqlfluff format {{[-d|--dialect]}} {{방언}} {{경로/대상/파일_또는_디렉터리}}`

- SQL 파일 또는 디렉터리의 지정한 린트 규칙 위반을 자동으로 수정:

`sqlfluff fix {{[-d|--dialect]}} {{방언}} {{[-r|--rules]}} {{규칙1,규칙2,...}} {{경로/대상/파일_또는_디렉터리}}`

- SQL 파일 또는 디렉터리를 파싱하고 parse 트리 표시:

`sqlfluff parse {{[-d|--dialect]}} {{방언}} {{경로/대상/파일_또는_디렉터리}}`

- 지원되는 모든 SQL 방언 목록 표시:

`sqlfluff dialects`
