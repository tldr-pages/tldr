# minio server

> MinIO S3 호환 오브젝트 스토리지 엔진을 실행하는 서버 명령어.
> 더 많은 정보: <https://docs.min.io/enterprise/aistor-object-store/reference/aistor-server/>.

- 기본 설정으로 MinIO 서버 시작:

`minio server {{경로/대상/데이터_디렉터리}}`

- API 포트와 웹 콘솔 포트를 지정하여 서버 시작:

`minio server --address ":{{포트}}" --console-address ":{{포트}}" {{경로/대상/데이터_디렉터리}}`

- 2개 노드 클러스터의 일부로 서버 시작:

`minio server {{노드1_호스트명}} {{경로/대상/데이터_디렉터리}} {{노드2_호스트명}} {{경로/대상/데이터_디렉터리}}`
