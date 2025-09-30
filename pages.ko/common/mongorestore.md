# mongorestore

> 컬렉션이나 데이터베이스를 바이너리 덤프에서 MongoDB 인스턴스로 가져오기 위한 유틸리티.
> 더 많은 정보: <https://docs.mongodb.com/database-tools/mongorestore/>.

- BSON 데이터 덤프를 디렉토리에서 MongoDB 데이터베이스로 가져오기:

`mongorestore --db {{데이터베이스_이름}} {{경로/대상/폴더}}`

- 사용자인증을 통해, 특정 포트에서 실행 중인 MongoDB 서버 호스트의 지정된 데이터베이스로 디렉토리의 BSON 데이터 덤프 가져오기 (사용자는 비밀번호를 묻게 됩니다):

`mongorestore --host {{데이터베이스_호스트:포트}} --db {{데이터베이스_이름}} --username {{사용자_명}} {{경로/대상/폴더}} --password`

- BSON 파일에서 MongoDB 데이터베이스로 컬렉션 가져오기:

`mongorestore --db {{데이터베이스_이름}} {{경로/대상/파일}}`

- 사용자인증을 통해, 특정 포트에서 실행 중인 MongoDB 서버 호스트의 지정된 데이터베이스로 BSON 파일에서 컬렉션 가져오기 (사용자는 비밀번호를 묻게 됩니다):

`mongorestore --host {{데이터베이스_호스트:포트}} --db {{데이터베이스_이름}} --username {{사용자_명}} {{경로/대상/파일}} --password`
