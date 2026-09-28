# uv run

> 프로젝트 환경에서 명령 또는 스크립트 실행.
> 더 많은 정보: <https://docs.astral.sh/uv/reference/cli/#uv-run>.

- Python 스크립트 실행:

`uv run {{경로/대상/스크립트.py}}`

- Python 모듈 실행:

`uv run {{[-m|--module]}} {{모듈_이름}}`

- 추가 패키지를 임시로 설치하여 명령 실행:

`uv run {{[-w|--with]}} {{패키지}} {{명령어}}`

- requirements 파일의 패키지를 사용하여 스크립트 실행:

`uv run --with-requirements {{경로/대상/requirements.txt}} {{경로/대상/스크립트.py}}`

- 격리된 환경에서 실행 (프로젝트 의존성 사용하지 않음):

`uv run --isolated {{경로/대상/스크립트.py}}`

- 환경을 먼저 동기화하지 않고 명령 실행:

`uv run --no-sync {{명령어}}`
