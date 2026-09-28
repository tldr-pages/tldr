# poetry-env

> Poetry 프로젝트와 연결된 가상 환경을 관리.
> 관련 항목: `asdf`.
> 더 많은 정보: <https://python-poetry.org/docs/cli/#env>.

- 가상 환경을 활성화하는 명령 출력:

`poetry env activate`

- 현재 환경 정보 표시:

`poetry env info`

- 현재 환경의 경로 표시:

`poetry env info {{[-p|--path]}}`

- 현재 환경의 Python 실행 파일 경로 표시:

`poetry env info {{[-e|--executable]}}`

- 현재 프로젝트와 연결된 모든 가상 환경 목록 표시  (전체 경로를 포함):

`poetry env list --full-path`

- 현재 프로젝트와 연결된 특정 또는 모든 가상 환경 제거:

`poetry env remove python {{경로/대상/실행파일|환경_이름}} | poetry env remove --all`

- 지정한 Python 실행 파일을 사용하여 프로젝트 가상 환경 활성화 또는 생성:

`poetry env use python {{경로/대상/실행파일}}`
