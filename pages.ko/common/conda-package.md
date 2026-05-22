# conda package

> 저수준 conda 패키지 생성.
> 더 많은 정보: <https://docs.conda.io/projects/conda/en/stable/commands/package.html>.

- 파일로부터 conda 패키지 확인:

`conda package {{[-w|--which]}} {{경로/대상/파일}}`

- 추적되지 않는 모든 파일 제거:

`conda package {{[-r|--reset]}}`

- 추적되지 않는 모든 파일 표시:

`conda package {{[-u|--untracked]}}`

- 생성할 패키지의 이름 지정:

`conda package --pkg-name {{이름}}`

- 생성할 패키지의 버전 지정:

`conda package --pkg-version {{버전}}`

- 생성할 패키지의 빌드 번호 지정:

`conda package --pkg-build {{빌드_번호}}`
