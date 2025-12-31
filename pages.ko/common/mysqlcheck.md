# mysqlcheck

> MySQL 테이블 검사 및 복구.
> 더 많은 정보: <https://dev.mysql.com/doc/refman/en/mysqlcheck.html>.

- 테이블 검사:

`mysqlcheck --check {{테이블}}`

- 테이블을 검사하고 접근을 위한 인증 정보 제공:

`mysqlcheck --check {{테이블}} --user {{사용자_명}} --password {{비밀번호}}`

- 테이블 복구:

`mysqlcheck --repair {{테이블}}`

- 테이블 최적화:

`mysqlcheck --optimize {{테이블}}`
