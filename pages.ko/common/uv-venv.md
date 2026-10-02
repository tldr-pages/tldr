# uv venv

> 패키지 설치 목적의 격리된 Python 가상 환경을 생성.
> 더 많은 정보: <https://docs.astral.sh/uv/reference/cli/#uv-venv>.

- 기본 위치(`.venv`)에 가상 환경 생성:

`uv venv`

- 지정한 경로에 가상 환경 생성:

`uv venv {{경로/대상/가상환경}}`

- 지정한 Python 버전을 사용해 가상 환경 생성:

`uv venv {{[-p|--python]}} {{3.12}}`

- `pip` 등 기본 패키지를 포함하여 가상 환경 생성:

`uv venv --seed`

- 사용자 지정 프롬프트 접두사 사용해 가상 환경 생성:

`uv venv --prompt {{자신의_프로젝트}}`

- 기존 가상 환경 덮어쓰기 허용 후 생성:

`uv venv --allow-existing {{가상환경_이름}}`
