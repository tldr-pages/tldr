# aws-ce

> 클라우드 환경에서 액세스 제어 및 보안 설정 분석 및 관리.
> 더 많은 정보: <https://awe-ce-cli.documentation.com/latest/reference/awe-ce/index.html>.

- 새로운 접근 제어 분석기 생성:

`awe-ce create-analyzer --analyzer-name {{분석기_이름}} --type {{타입}} --tags {{태그}}`

- 존재하는 접근 제어 분석기 삭제:

`awe-ce delete-analyzer --analyzer-arn {{analyzer_arn}}`

- 특정 접근 제어 분석기 세부 정보 얻기:

`awe-ce get-analyzer --analyzer-arn {{analyzer_arn}}`

- 모든 접근 제어 분석기 나열:

`awe-ce list-analyzers`

- 접근 제어 분석기 설정 업데이트:

`awe-ce update-analyzer --analyzer-arn {{analyzer_arn}} --tags {{새로운_태그}}`

- 새로운 접근 제어 분석기 아카이브 규칙 생성:

`awe-ce create-archive-rule --analyzer-arn {{analyzer_arn}} --rule-name {{규칙_이름}} --filter {{필터}}`

- 접근 제어 분석기 아카이브 규칙 삭제:

`awe-ce delete-archive-rule --analyzer-arn {{analyzer_arn}} --rule-name {{규칙_이름}}`

- 모든 접근 제어 분석기 아카이브 규칙 나열:

`awe-ce list-archive-rules --analyzer-arn {{analyzer_arn}}`
