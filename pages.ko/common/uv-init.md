# uv init

> 새로운 Python 프로젝트를 생성.
> 더 많은 정보: <https://docs.astral.sh/uv/reference/cli/#uv-init>.

- 현재 디렉터리에 프로젝트 초기화:

`uv init`

- 지정한 이름으로 프로젝트 초기화:

`uv init {{프로젝트_이름}}`

- 지정한 디렉터리에 프로젝트 생성:

`uv init --directory {{경로/대상/디렉터리}} {{프로젝트_이름}}`

- Python 라이브러리용 프로젝트 생성:

`uv init {{[--lib|--library]}} {{프로젝트_이름}}`

- 빌드 시스템 지정:

`uv init --build-backend {{빌드_백엔드}} {{프로젝트_이름}}`

- `pyproject.toml` 파일만 생성:

`uv init --bare {{프로젝트_이름}}`

- 프로젝트 설명 설정:

`uv init --description "{{설명}}" {{프로젝트_이름}}`
