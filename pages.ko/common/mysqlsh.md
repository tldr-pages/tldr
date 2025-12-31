# mysqlsh

> SQL, JavaScript, Python을 지원하는 MySQL의 고급 명령줄 클라이언트.
> InnoDB 클러스터 및 문서 저장소 컬렉션 관리를 위한 기능 제공.
> 더 많은 정보: <https://manned.org/mysqlsh>.

- 대화형 모드로 MySQL Shell 시작:

`mysqlsh`

- MySQL 서버에 연결:

`mysqlsh --user {{사용자_명}} --host {{호스트_명}} --port {{포트}}`

- 서버에서 SQL 문을 실행하고 종료:

`mysqlsh --user {{사용자_명}} --execute '{{sql_문}}'`

- JavaScript 모드로 MySQL Shell 시작:

`mysqlsh --js`

- Python 모드로 MySQL Shell 시작:

`mysqlsh --py`

- JSON 문서를 MySQL 컬렉션에 가져오기:

`mysqlsh --import {{경로/대상/파일.json}} --schema {{스키마_명}} --collection {{컬렉션_명}}`

- 상세 출력 활성화:

`mysqlsh --verbose`
