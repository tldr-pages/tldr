# hatch

> 현대적이고 확장 가능한 Python 프로젝트 관리자.
> 관련 항목: `poetry`.
> 더 많은 정보: <https://hatch.pypa.io/latest/cli/reference/>.

- 새로운 Hatch 프로젝트 생성:

`hatch new {{프로젝트_이름}}`

- 기존 프로젝트에 Hatch 초기화:

`hatch new --init`

- Hatch 프로젝트 빌드:

`hatch build`

- 빌드 결과물 제거:

`hatch clean`

- `pyproject.toml` 파일에 정의된 의존성을 사용하여 기본 환경 생성:

`hatch env create`

- 환경 의존성을 테이블 형태로 표시:

`hatch dep show table`
