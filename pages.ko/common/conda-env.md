# conda env

> conda 환경 관리.
> 더 많은 정보: <https://docs.conda.io/projects/conda/en/latest/commands/env/index.html>.

- 환경 설정 파일(YAML, TXT 등)을 통해 환경 생성:

`conda env create {{[-f|--file]}} {{경로/대상/파일}}`

- 환경 및 내부 모든 항목 삭제:

`conda env remove {{[-n|--name]}} {{환경_이름}}`

- 환경 파일을 기반으로 환경을 업데이트:

`conda env update {{[-f|--file]}} {{경로/대상/파일}} --prune`

- 모든 환경 목록 표시:

`conda env list`

- 환경 상세 정보 확인:

`conda env export`

- 환경 변수 목록 표시:

`conda env config vars list`

- 환경 변수 설정:

`conda env config vars set {{환경변수_키}}={{값}}`
