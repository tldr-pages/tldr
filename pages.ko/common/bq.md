# bq

> Google Cloud의 완전 관리형 서버리스 엔터프라이즈 데이터 웨어하우스인 BigQuery용 Python 기반 도구.
> 더 많은 정보: <https://cloud.google.com/bigquery/docs/reference/bq-cli-reference>.

- 표준 SQL을 사용하여 BigQuery 테이블에 대해 쿼리를 실행하고, `--dry_run` 플래그를 추가해 쿼리에서 읽은 바이트 수를 추정:

`bq query --nouse_legacy_sql 'SELECT COUNT(*) FROM {{데이터셋_이름}}.{{테이블_이름}}'`

- 매개변수화된 쿼리 실행:

`bq query --use_legacy_sql=false --parameter='ts_value:TIMESTAMP:2016-12-07 08:00:00' 'SELECT TIMESTAMP_ADD(@ts_value, INTERVAL 1 HOUR)'`

- 미국 위치에 새 데이터 세트 또는 테이블을 만듬:

`bq mk --location=US {{dataset_name}}.{{table_name}}`

- 프로젝트의 모든 데이터세트를 나열:

`bq ls --filter labels.{{키}}:{{값}} --max_results {{정수}} --format=prettyjson --project_id {{프로젝트_아이디}}`

- CSV, JSON, Parquet, Avro 등의 형식으로 특정 파일의 데이터를 테이블에 일괄 로드:

`bq load --location {{위치}} --source_format {{CSV|JSON|PARQUET|AVRO}} {{데이터셋}}.{{테이블}} {{경로_대상_소스}}`

- 한 테이블을 다른 테이블에 복사:

`bq cp {{데이터셋}}.{{오래된_테이블}} {{데이터셋}}.{{새로운_테이블}}`

- 버전 정보 표시:

`bq help`
