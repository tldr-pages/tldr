# mc

> 객체 스토리지 및 파일 시스템용 MinIO Client.
> 일부 시스템에선 `mc` 또는 `mcli`라는 이름으로 제고오딤.
> 더 많은 정보: <https://minio.github.io/mc/>.

- S3 서버 연결 정보 추가:

`mc alias set {{로컬}} {{http://localhost:9000}} {{액세스_키}} {{비밀_키}}`

- 버킷 생성:

`mc mb {{로컬/버킷_이름}}`

- 버킷 및 내부 객체를 재귀적으로 조회:

`mc ls {{로컬}} --recursive`
