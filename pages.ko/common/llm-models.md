# llm models

> `llm` 명령에서 사용할 수 있는 모델 관리.
> 더 많은 정보: <https://llm.datasette.io/en/stable/help.html#llm-models-help>.

- 사용 가능한 모든 모델 나열:

`llm models list`

- 검색어 쿼리와 일치하는 모델 나열:

`llm models list {{[-q|--query]}} {{gpt}}`

- 도구를 지원하는 모델 나열:

`llm models list --tools`

- 지원되는 옵션과 함께 모델 나열:

`llm models list --options`

- 현재 기본 모델 표시:

`llm models default`

- 기본 모델 설정:

`llm models default {{모델_id_또는_별칭}}`
