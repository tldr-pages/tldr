# dvc add

> 변경된 파일을 색인에 추가.
> 더 많은 정보: <https://dvc.org/doc/command-reference/add>.

- 단일 대상 파일을 색인에 추가:

`dvc add {{경로/대상/파일}}`

- 대상 디렉토리를 색인에 추가:

`dvc add {{경로/대상/폴더}}`

- 주어진 대상 디렉토리의 모든 파일을 재귀적으로 추가:

`dvc add --recursive {{경로/대상/폴더}}`

- 사용자 정의 `.dvc` 파일 이름으로 대상 파일 추가:

`dvc add --file {{custom_name.dvc}} {{경로/대상/파일}}`
