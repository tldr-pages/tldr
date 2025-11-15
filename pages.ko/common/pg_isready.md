# pg_isready

> PostgreSQL 서버의 연결 상태 확인.
> 더 많은 정보: <https://www.postgresql.org/docs/current/app-pg-isready.html>.

- 연결 상태 확인:

`pg_isready`

- 특정 호스트명과 포트를 사용하여 연결 상태 확인:

`pg_isready --host={{호스트명}} --port={{포트}}`

- 연결 실패 시에만 메시지 표시하며 연결 상태 확인:

`pg_isready --quiet`
