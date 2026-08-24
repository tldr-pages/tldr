# conda compare

> conda 환경 간 패키지 비교.
> 더 많은 정보: <https://docs.conda.io/projects/conda/en/stable/commands/compare.html>.

- 현재 디렉터리의 패키지와 `file.yml` 파일 패키지 비교:

`conda compare file.yml`

- `myenv` 환경의 패키지와 `file.yml` 파일의 패키지 비교:

`conda compare {{[-n|--name]}} myenv {{경로/대상/파일.yml}}`

- 사용자 지정 경로(prefix)에 있는 `myenv` 환경의 패키지와 `file.yml` 파일의 패키지 비교:

`conda compare {{[-p|--prefix]}} {{경로/대상/myenv}} {{경로/대상/파일.yml}}`

- 도움말 표시:

`conda compare {{[-h|--help]}}`
