# conda config

> `.condarc`의 설정 값을 수정.
> 더 많은 정보: <https://docs.conda.io/projects/conda/en/latest/commands/config.html>.

- 모든 설정 값 표시:

`conda config --show`

- 특정 설정 옵션의 현재 값 표시:

`conda config --show {{설정_옵션}}`

- 설정 값 지정:

`conda config --set {{키}} {{값}}`

- 설정 값 제거:

`conda config --remove {{키}} {{값}}`

- 기존 설정 키 목록의 끝에 값 추가:

`conda config --append {{키}} {{값}}`

- 기존 설정 키 목록의 앞에 값 추가:

`conda config --prepend {{키}} {{값}}`

- 지정한 설정 옵션 설명 표시:

`conda config --describe {{설정_옵션}}`
