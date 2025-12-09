# mongod

> MongoDB 데이터베이스 서버.
> 더 많은 정보: <https://docs.mongodb.com/manual/reference/program/mongod>.

- 저장 디렉터리 지정 (기본값: Linux 및 macOS는 `/data/db`, Windows는 `C:\data\db`):

`mongod --dbpath {{경로/대상/폴더}}`

- 설정 파일 지정:

`mongod --config {{경로/대상/파일}}`

- 청취할 포트 지정 (기본값: 27017):

`mongod --port {{포트}}`

- 데이터베이스 프로파일링 수준 지정. 0은 꺼짐, 1은 느린 작업만, 2는 모든 작업 (기본값: 0):

`mongod --profile {{0|1|2}}`
