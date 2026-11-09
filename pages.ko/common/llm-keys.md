# llm keys

> 다양한 모델에 대해 저장된 API 키를 관리.
> 더 많은 정보: <https://llm.datasette.io/en/stable/help.html#llm-keys-help>.

- 저장된 모든 키 이름 나열:

`llm keys list`

- 모델 제공자의 API 키 저장 (키 입력을 요청받음):

`llm keys set {{openai}}`

- 저장된 키 값 출력:

`llm keys get {{openai}}`

- 키가 저장된 `keys.json` 파일의 경로 출력:

`llm keys path`
