# conda export

> 환경 상세 정보 내보내기.
> 더 많은 정보: <https://docs.conda.io/projects/conda/en/latest/commands/export.html>.

- 현재 환경의 상세 정보를 `stdout`으로 출력:

`conda export`

- 현재 환경의 상세 정보를 `YAML` 파일로 내보내기:

`conda export {{[-f|--file]}} {{경로/대상/환경.yaml}}`

- 특정 형식으로 상세 정보 내보내기:

`conda export --format {{environment-json|environment-yaml|explicit|json|reqs|requirements|txt|yaml|yml}}`

- 이름으로 환경을 지정:

`conda export {{[-n|--name]}} {{환경_이름}}`

- 경로로 환경 지정:

`conda export {{[-p|--prefix]}} {{경로/대상/환경}}`

- 특정 채널 포함:

`conda export {{[-c|--channel]}} {{채널_이름}}`
