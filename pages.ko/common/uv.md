# uv

> 빠른 Python 패키지 및 프로젝트 관리자.
> `tool`, `python`과 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
> 더 많은 정보: <https://docs.astral.sh/uv/reference/cli/>.

- 현재 디렉터리에 새 Python 프로젝트 생성:

`uv init`

- 지정한 경로에 새 Python 프로젝트 생성:

`uv init {{경로/대상/디렉터리}}`

- 프로젝트에 새 의존성 패키지 추가:

`uv add {{패키지}}`

- 프로젝트에서 의존성 패키지 제거:

`uv remove {{패키지}}`

- 프로젝트 환경에서 스크립트 또는 명령 실행:

`uv run {{경로/대상/스크립트.py|명령어}}`

- `pyproject.toml`을 기반으로 프로젝트 환경 업데이트:

`uv sync`

- 프로젝트 의존성을 위한 lock 파일 생성:

`uv lock`

- 프로젝트를 소스 및 바이너리 배포판으로 빌드:

`uv build`
