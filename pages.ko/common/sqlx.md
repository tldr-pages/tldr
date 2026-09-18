# sqlx

> Rust SQL 툴킷인 SQLx의 유틸리티.
> 더 많은 정보: <https://github.com/launchbadge/sqlx/blob/main/sqlx-cli/README.md>.

- `$DATABASE_URL` 환경 변수에 지정된 데이터베이스 생성:

`sqlx database create`

- 지정한 데이터베이스 삭제:

`sqlx database drop {{[-D|--database-url]}} {{데이터베이스_주소}}`

- "migrations" 디렉터리에 지정한 설명으로 up/down 마이그레이션 파일 쌍 생성:

`sqlx migrate add -r {{마이그레이션_내용}}`

- 지정한 데이터베이스에 아직 적용되지 않은 모든 마이그레이션 실행:

`sqlx migrate run {{[-D|--database-url]}} {{데이터베이스_주소}}`

- 지정한 데이터베이스의 가장 최근 마이그레이션 되돌리기:

`sqlx migrate revert {{[-D|--database-url]}} {{데이터베이스_주소}}`
