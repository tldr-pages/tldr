# dolt sql

> SQL 쿼리를 실행. 여러 SQL 문은 세미콜론으로 구분해야 함.
> 더 많은 정보: <https://docs.dolthub.com/cli-reference/cli#dolt-sql>.

- 단일 쿼리 실행:

`dolt sql --query "{{INSERT INTO t values (1, 3);}}"`

- 저장된 모든 쿼리를 나열:

`dolt sql --list-saved`
