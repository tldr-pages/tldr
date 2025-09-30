# neo4j-admin

> Neo4j DBMS(데이터베이스 관리 시스템) 관리 및 운영.
> 같이 보기: `cypher-shell`, `mysqld`.
> 더 많은 정보: <https://neo4j.com/docs/operations-manual/current/neo4j-admin-neo4j-cli/>.

- DBMS 시작:

`neo4j-admin server start`

- DBMS 중지:

`neo4j-admin server stop`

- 기본 `neo4j` 사용자의 초기 비밀번호 설정 (DBMS를 처음 시작하기 위한 전제 조건):

`neo4j-admin dbms set-initial-password {{데이터베이스_이름}}`

- 오프라인 데이터베이스의 아카이브(덤프)를 `database_name.dump`라는 이름의 파일로 생성:

`neo4j-admin database dump --to-path={{경로/대상/폴더}} {{데이터베이스_이름}}`

- `database_name.dump`라는 아카이브에서 데이터베이스 로드:

`neo4j-admin database load --from-path={{경로/대상/폴더}} {{데이터베이스_이름}} --overwrite-destination=true`

- 지정된 아카이브 파일을 `stdin`을 통해 데이터베이스 로드:

`neo4j-admin database load --from-stdin {{데이터베이스_이름}} --overwrite-destination=true < {{경로/대상/파일이름.dump}}`

- 도움말 표시:

`neo4j-admin --help`
