# dvc commit

> 프로젝트에서 DVC로 추적되는 파일의 변경 사항 기록.
> 더 많은 정보: <https://dvc.org/doc/command-reference/commit>.

- 모든 DVC로 추적된 파일과 디렉토리의 변경 사항 커밋:

`dvc commit`

- 지정된 DVC로 추적된 대상의 변경 사항 커밋:

`dvc commit {{대상}}`

- 디렉토리 내의 모든 DVC로 추적된 파일을 재귀적으로 커밋:

`dvc commit --recursive {{경로/대상/폴더}}`
