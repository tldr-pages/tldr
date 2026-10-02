# uv lock

> 프로젝트의 lockfile 업데이트.
> 더 많은 정보: <https://docs.astral.sh/uv/reference/cli/#uv-lock>.

- 프로젝트의 lockfile 생성 또는 업데이트:

`uv lock`

- lockfile 변경하지 않고 최신 상태인지 확인:

`uv lock --check`

- 최신 상태인지는 확인하지 않고 lockfile이 존재하는지만 확인:

`uv lock --check-exists`

- lockfile을 작성하지 않고 잠길 내용을 미리 확인:

`uv lock --dry-run`

- 현재 프로젝트 대신 지정한 Python 스크립트의 의존성 잠금:

`uv lock --script {{경로/대상/스크립트.py}}`

- 모든 패키지를 호환 가능한 최신 버전으로 업그레이드:

`uv lock --upgrade`

- 지정한 패키지만 업그레이드:

`uv lock --upgrade-package {{패키지1}} --upgrade-package {{패키지2}}`
