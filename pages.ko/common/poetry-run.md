# poetry run

> 프로젝트의 가상 환경에서 명령을 실행.
> 더 많은 정보: <https://python-poetry.org/docs/cli/#run>.

- 가상 환경에서 명령 실행:

`poetry run {{명령어}}`

- 인수를 전달하여 명령을 실행:

`poetry run {{명령어}} {{인자1 인자2 ...}}`

- `pyproject.toml`에 정의된 스크립트 실행:

`poetry run {{스크립트_이름}}`

- Python 스크립트 실행:

`poetry run python {{경로/대상/스크립트.py}}`
