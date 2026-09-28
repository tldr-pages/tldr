# uv sync

> 프로젝트 환경을 lockfile과 일치하도록 업데이트.
> 더 많은 정보: <https://docs.astral.sh/uv/reference/cli/#uv-sync>.

- 프로젝트 환경을 lockfile과 동기화:

`uv sync`

- 모든 선택적 의존성을 포함하여 동기화:

`uv sync --all-extras`

- 지정한 선택적 의존성을 포함하여 동기화:

`uv sync --extra {{선택_의존성_이름}}`

- 개발 의존성만 동기화:

`uv sync --only-dev`

- 개발 의존성을 제외하고 동기화:

`uv sync --no-dev`

- 지정한 의존성 그룹을 동기화:

`uv sync --group {{그룹_이름}}`

- 환경이 이미 동기화되어 있는지 확인 (변경 없이):

`uv sync --check`

- 실제 변경 없이 동기화될 내용을 미리 확인:

`uv sync --dry-run`
