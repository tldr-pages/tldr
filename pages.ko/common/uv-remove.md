# uv remove

> 프로젝트의 `pyproject.toml` 파일에서 의존성을 제거.
> 더 많은 정보: <https://docs.astral.sh/uv/reference/cli/#uv-remove>.

- 프로젝트에서 의존성을 제거:

`uv remove {{패키지}}`

- 여러 의존성 제거:

`uv remove {{패키지1 패키지2 ...}}`

- 개발 의존성 제거:

`uv remove --dev {{패키지}}`

- 선택적인 의존성 그룹에서 의존성 제거:

`uv remove --optional {{선택_의존성_이름}} {{패키지}}`

- 지정한 의존성 그룹에서 의존성 제거:

`uv remove --group {{그룹_이름}} {{패키지}}`

- 가상 환경을 동기화하지 않고 의존성 제거:

`uv remove --no-sync {{패키지}}`
