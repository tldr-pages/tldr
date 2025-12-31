# pgbench

> PostgreSQL에 대한 벤치마크 테스트 실행.
> 더 많은 정보: <https://www.postgresql.org/docs/current/pgbench.html>.

- 기본 크기의 50배로 데이터베이스 초기화:

`pgbench --initialize --scale={{50}} {{데이터베이스_이름}}`

- 10명의 클라이언트, 2개의 작업 스레드, 클라이언트당 10,000개의 트랜잭션으로 데이터베이스 벤치마크 실행:

`pgbench --client={{10}} --jobs={{2}} --transactions={{10000}} {{데이터베이스_이름}}`
