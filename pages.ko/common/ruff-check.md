# ruff check

> 매우 빠른 Python 린터입니다. `check`는 기본 명령어로, 어디서든 생략 가능합니다.
> 파일이나 디렉토리를 지정하지 않으면 기본적으로 현재 작업 디렉토리가 사용됩니다.
> 더 많은 정보: <https://docs.astral.sh/ruff/linter>.

- 지정된 파일이나 디렉토리에 대해 린터 실행:

`ruff check {{경로/대상/파일_또는_디렉토리1 경로/대상/파일_또는_디렉토리2 ...}}`

- 제안된 수정을 적용하여 파일을 직접 수정:

`ruff check --fix`

- 린터를 실행하고 변경 시 다시 린트:

`ruff check --watch`

- 설정 파일을 무시하고 지정된 규칙(또는 모든 규칙)만 활성화:

`ruff check --select {{ALL|규칙_코드1,규칙_코드2,...}}`

- 추가로 지정된 규칙 활성화:

`ruff check --extend-select {{규칙_코드1,규칙_코드2,...}}`

- 지정된 규칙 비활성화:

`ruff check --ignore {{규칙_코드1,규칙_코드2,...}}`

- `# noqa` 지시어를 추가하여 규칙의 모든 기존 위반 사항 무시:

`ruff check --select {{규칙_코드}} --add-noqa`
