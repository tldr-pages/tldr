# snowsql

> Snowflake의 데이터 클라우드를 위한 SnowSQL 커맨드라인 클라이언트.
> 더 많은 정보: <https://docs.snowflake.com/en/user-guide/snowsql.html>.

- <https://account.snowflakecomputing.com>의 특정 인스턴스에 연결 (비밀번호는 프롬프트 또는 설정 파일에서 제공 가능):

`snowsql --accountname {{계정}} --username {{사용자명}} --dbname {{데이터베이스}} --schemaname {{스키마}}`

- 특정 설정 파일에 지정된 인스턴스에 연결 (기본값은 `~/.snowsql/config`):

`snowsql --config {{경로/대상/설정_파일}}`

- 다단계 인증 토큰을 사용하여 기본 인스턴스에 연결:

`snowsql --mfa-passcode {{토큰}}`

- 기본 연결에서 단일 SQL 쿼리 또는 SnowSQL 명령 실행 (쉘 스크립트에서 유용):

`snowsql --query '{{쿼리}}'`

- 특정 파일에서 기본 연결로 명령 실행:

`snowsql --filename {{경로/대상/파일.sql}}`
