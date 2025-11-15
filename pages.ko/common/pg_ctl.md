# pg_ctl

> PostgreSQL 서버 및 데이터베이스 클러스터를 제어하는 유틸리티.
> 더 많은 정보: <https://www.postgresql.org/docs/current/app-pg-ctl.html>.

- 새로운 PostgreSQL 데이터베이스 클러스터 초기화:

`pg_ctl -D {{데이터_디렉토리}} init`

- PostgreSQL 서버 시작:

`pg_ctl -D {{데이터_디렉토리}} start`

- PostgreSQL 서버 중지:

`pg_ctl -D {{데이터_디렉토리}} stop`

- PostgreSQL 서버 재시작:

`pg_ctl -D {{데이터_디렉토리}} restart`

- PostgreSQL 서버 설정 다시 로드:

`pg_ctl -D {{데이터_디렉토리}} reload`
