# aws accessanalyzer

> 잠재적인 보안 위험을 파악하기 위해, 리소스 정책을 분석하고 검토.
> 더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/index.html>.

- 새로운 Access Analyzer 생성:

`aws accessanalyzer create-analyzer --analyzer-name {{분석기_이름}} --type {{타입}} --tags {{태그}}`

- 기존 Access Analyzer 삭제:

`aws accessanalyzer delete-analyzer --analyzer-arn {{analyzer_arn}}`

- 특정 Access Analyzer 세부 정보 출력:

`aws accessanalyzer get-analyzer --analyzer-arn {{analyzer_arn}}`

- 모든 Access Analyzers 나열:

`aws accessanalyzer list-analyzers`

- Access Analyzer 설정 업데이트:

`aws accessanalyzer update-analyzer --analyzer-arn {{analyzer_arn}} --tags {{new_tags}}`

- 새로운 Access Analyzer 아카이브 규칙 생성:

`aws accessanalyzer create-archive-rule --analyzer-arn {{analyzer_arn}} --rule-name {{규칙_이름}} --filter {{filter}}`

- Access Analyzer 아카이브 규칙 삭제:

`aws accessanalyzer delete-archive-rule --analyzer-arn {{analyzer_arn}} --rule-name {{rule_name}}`

- 모든 Access Analyzer 아카이브 규칙 나열:

`aws accessanalyzer list-archive-rules --analyzer-arn {{analyzer_arn}}`
