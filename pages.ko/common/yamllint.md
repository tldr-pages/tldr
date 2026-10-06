# yamllint

> YAML 파일 검사하는 린터.
> 더 많은 정보: <https://yamllint.readthedocs.io>.

- 파일 린트:

`yamllint {{경로/대상/파일.yaml}}`

- 디렉터리의 모든 YAML 파일을 재귀적으로 린트:

`yamllint {{경로/대상/디렉터리}}`

- 지정한 설정 파일을 사용하여 파일 린트:

`yamllint {{[-c|--config-file]}} {{경로/대상/설정파일.yaml}} {{경로/대상/파일.yaml}}`

- 사전 정의된 설정을 사용하여 파일 린트 (`default` 또는 `relaxed`):

`yamllint {{[-d|--config-data]}} "{{extends: relaxed}}" {{경로/대상/파일.yaml}}`

- 파싱 가능한 형식으로 결과 출력 (CI 통합에 유용):

`yamllint {{[-f|--format]}} parsable {{경로/대상/파일.yaml}}`

- 엄격 모드로 파일 린트 (경고 발생 시 종료 코드 2 반환):

`yamllint {{[-s|--strict]}} {{경로/대상/파일.yaml}}`

- `stdin`에서 YAML을 읽어 린트:

`cat {{경로/대상/파일.yaml}} | yamllint -`

- 도움말 표시:

`yamllint {{[-h|--help]}}`
