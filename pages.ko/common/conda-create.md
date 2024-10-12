# conda create

> 새로운 conda 환경을 생성.
> 더 많은 정보: <https://docs.conda.io/projects/conda/en/latest/commands/create.html>.

- `py39`라는 새로운 환경을 만들고, 여기에 Python 3.9 및 NumPy v1.11 이상을 설치:

`conda create --yes --name {{py39}} python={{3.9}} "{{numpy>=1.11}}"`

- 환경의 완벽한 복사본 생성:

`conda create --clone {{py39}} --name {{py39-copy}}`

- 지정된 이름으로 새 환경을 만들고 지정된 패키지를 설치:

`conda create --name {{환경_이름}} {{패키지}}`
