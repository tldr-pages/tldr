# gh workflow

> GitHub Actions 워크플로우를 나열, 보기 및 실행.
> 더 많은 정보: <https://cli.github.com/manual/gh_workflow>.

- 상호작용식으로 워크플로우를 선택하여 최신 작업 보기:

`gh workflow view`

- 기본 브라우저에서 특정 워크플로우 보기:

`gh workflow view {{id|workflow_name|filename.yml}} --web`

- 특정 워크플로우의 YAML 정의 표시:

`gh workflow view {{id|workflow_name|filename.yml}} --yaml`

- 특정 Git 브랜치 또는 태그의 YAML 정의 표시:

`gh workflow view {{id|workflow_name|filename.yml}} --ref {{branch|tag_name}} --yaml`

- 워크플로우 파일 나열 (`--all`을 사용하여 비활성 워크플로우 포함 가능):

`gh workflow list`

- 매개변수와 함께 수동으로 워크플로우 실행:

`gh workflow run {{id|workflow_name|filename.yml}} {{--raw-field param1=value1 --raw-field param2=value2 ...}}`

- 특정 브랜치 또는 태그를 사용하여 `stdin`에서 JSON 매개변수로 수동 워크플로우 실행:

`echo '{{{"param1": "value1", "param2": "value2", ...}}}' | gh workflow run {{id|workflow_name|filename.yml}} --ref {{branch|tag_name}}`

- 특정 워크플로우 활성화 또는 비활성화:

`gh workflow {{enable|disable}} {{id|workflow_name|filename.yml}}`
