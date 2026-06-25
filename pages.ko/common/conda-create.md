# conda create

> 새로운 conda 환경을 생성.
> 더 많은 정보: <https://docs.conda.io/projects/conda/en/latest/commands/create.html>.

- `py39`라는 새로운 환경을 생성하고, Python 3.9, NumPy v1.11 이상을 설치하며, SciPy 최신 안정 버전 설치 및 모든 확인에 자동으로 yes 응답을 처리:

`conda create {{[-ny|--name --yes]}} py39 python=3.9 "numpy>=1.11 scipy"`

- `myenv`라는 새로운 환경을 생성하고 파일에 정의된 패키지 설치:

`conda create {{[-n|--name]}} myenv --file {{file1.yml}} --file {{file2.yml}}`

- 사용자 지정 경로(prefix)에 새로운 환경 생성:

`conda create {{[-p|--prefix]}} {{path/to/myenv}}`

- `py39` 환경과 일치하는 복사본 생성:

`conda create --clone py39 {{[-n|--name]}} {{py39-copy}}`

- 도움말 표시:

`conda create {{[-h|--help]}}`
