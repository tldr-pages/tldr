# dbt

> 데이터 웨어하우스에서 데이터 변환을 모델링하기 위한 도구.
> 더 많은 정보: <https://github.com/dbt-labs/dbt-core>.

- dbt 프로젝트와 데이터베이스 연결을 디버그:

`dbt debug`

- 프로젝트의 모든 모델을 실행:

`dbt run`

- `example_model`의 모든 테스트를 실행:

`dbt test --select example_model`

- `example_model`과 그 하위 의존 모델을 빌드 (시드 로드, 모델 실행, 스냅샷 및 테스트):

`dbt build --select example_model+`

- `not_now` 태그가 있는 모델을 제외하고 모든 모델을 빌드:

`dbt build --exclude "tag:not_now"`

- `one`과 `two` 태그를 모두 가진 모델을 빌드:

`dbt build --select "tag:one,tag:two"`

- `one` 또는 `two` 태그를 가진 모델을 빌드:

`dbt build --select "tag:one tag:two"`
