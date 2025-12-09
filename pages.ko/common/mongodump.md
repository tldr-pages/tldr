# mongodump

> MongoDB 인스턴스의 내용을 내보내는 유틸리티.
> 더 많은 정보: <https://docs.mongodb.com/database-tools/mongodump/>.

- 모든 데이터베이스의 덤프 생성 (파일은 "dump"라는 폴더에 저장됨):

`mongodump`

- 덤프의 출력 위치 지정:

`mongodump --out {{경로/대상/폴더}}`

- 특정 데이터베이스의 덤프 생성:

`mongodump --db {{데이터베이스_이름}}`

- 특정 데이터베이스 내의 특정 컬렉션 덤프 생성:

`mongodump --collection {{컬렉션_이름}} --db {{데이터베이스_이름}}`

- 주어진 포트에서 실행 중인 특정 호스트에 연결하여 덤프 생성:

`mongodump --host {{호스트}} --port {{포트}}`

- 특정 사용자 명으로 데이터베이스의 덤프 생성; 사용자에게 비밀번호 입력이 요청됨:

`mongodump --username {{사용자_명}} {{데이터베이스}} --password`

- 특정 인스턴스에서 덤프 생성; 호스트, 사용자, 비밀번호 및 데이터베이스가 연결 문자열에 정의됨:

`mongodump --uri {{연결_문자열}}`
