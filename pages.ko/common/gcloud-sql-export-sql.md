# gcloud sql export sql

> Cloud SQL 인스턴스에서 Google Cloud Storage의 SQL 파일로 데이터를 내보내기.
> 백업 생성이나 데이터 마이그레이션에 유용합니다. 같이 보기: `gcloud`.
> 더 많은 정보: <https://cloud.google.com/sdk/gcloud/reference/sql/export/sql>.

- 특정 Cloud SQL 인스턴스에서 Google Cloud Storage 버킷으로 데이터를 SQL 덤프 파일로 내보내기:

`gcloud sql export sql {{인스턴스}} gs://{{버킷_이름}}/{{파일_이름}}`

- 비동기적으로 데이터를 내보내고, 작업 완료를 기다리지 않고 즉시 반환:

`gcloud sql export sql {{인스턴스}} gs://{{버킷_이름}}/{{파일_이름}} --async`

- Cloud SQL 인스턴스 내 특정 데이터베이스에서 데이터 내보내기:

`gcloud sql export sql {{인스턴스}} gs://{{버킷_이름}}/{{파일_이름}} --database={{데이터베이스1,데이터베이스2,...}}`

- Cloud SQL 인스턴스 내의 지정된 데이터베이스에서 특정 테이블 내보내기:

`gcloud sql export sql {{인스턴스}} gs://{{버킷_이름}}/{{파일_이름}} --database={{데이터베이스}} --table={{테이블1,테이블2,...}}`

- 소스 인스턴스의 부담을 줄이기 위해 임시 인스턴스로 작업을 오프로드하여 데이터 내보내기:

`gcloud sql export sql {{인스턴스}} gs://{{버킷_이름}}/{{파일_이름}} --offload`

- 데이터를 내보내고 출력을 `gzip`으로 압축:

`gcloud sql export sql {{인스턴스}} gs://{{버킷_이름}}/{{파일_이름}}.gz`
