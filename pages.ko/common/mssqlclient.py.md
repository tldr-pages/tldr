# mssqlclient.py

> Microsoft SQL Server 인스턴스에 연결하고 쿼리를 실행.
> Impacket 도구 모음의 일부.
> 더 많은 정보: <https://github.com/fortra/impacket>.

- Windows 인증을 사용하여 MSSQL 서버에 연결:

`mssqlclient.py -windows-auth {{도메인}}/{{사용자명}}:{{비밀번호}}@{{대상_서버}}`

- SQL 서버 인증을 사용하여 연결:

`mssqlclient.py {{사용자명}}:{{비밀번호}}@{{대상_서버}}`

- 해시 기반 인증을 사용해 연결:

`mssqlclient.py {{도메인}}/{{사용자명}}@{{대상_서버}} -hashes {{LM_Hash}}:{{NT_Hash}}`

- Kerberos 인증을 사용하여 연결 (유효한 티켓 필요):

`mssqlclient.py -k {{도메인}}/{{사용자명}}@{{대상_서버}}`

- 연결 후 특정 SQL 명령 실행:

`mssqlclient.py {{사용자명}}:{{비밀번호}}@{{대상_서버}} -query "{{SELECT user_name();}}"`

- 파일에 있는 여러 SQL 명령 실행:

`mssqlclient.py {{사용자명}}:{{비밀번호}}@{{대상_서버}} -file {{경로/대상/sql_파일.sql}}`

- 특정 데이터베이스에 연결 (기본값: `None`):

`mssqlclient.py {{사용자명}}:{{비밀번호}}@{{대상_서버}} -db {{데이터베이스_이름}}`

- 실행 전에 SQL 쿼리 표시:

`mssqlclient.py {{사용자명}}:{{비밀번호}}@{{대상_서버}} -show`
