# cypher-shell

> 대화형 세션을 열고 Neo4j 인스턴스에 대해 Cypher 쿼리를 실행.
> 참고: `neo4j-admin`, `mysql`.
> 더 많은 정보: <https://neo4j.com/docs/operations-manual/current/tools/cypher-shell/>.

- 기본 포트에서 로컬 인스턴스에 연결 (`neo4j://localhost:7687`):

`cypher-shell`

- 원격 인스턴스에 연결:

`cypher-shell --address neo4j://{{호스트}}:{{포트}}`

- 보안 자격 증명 연결 및 제공:

`cypher-shell --username {{사용자명}} --password {{비밀번호}}`

- 특정 데이터베이스에 연결:

`cypher-shell --database {{데이터베이스_이름}}`

- 파일에서 Cypher 문을 실행하고 닫음:

`cypher-shell --file {{경로/대상/파일.cypher}}`

- 파일에 대한 로깅 활성화:

`cypher-shell --log {{경로/대상/파일.log}}`

- 도움말 표시:

`cypher-shell --help`
