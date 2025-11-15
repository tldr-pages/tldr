# mysqldump

> MySQL 데이터베이스 백업.
> 데이터베이스 복원에 대해서는 `mysql`을 참조하세요.
> 더 많은 정보: <https://dev.mysql.com/doc/refman/en/mysqldump.html>.

- 백업 생성 (사용자에게 비밀번호가 요청됨):

`mysqldump --user {{사용자_명}} --password {{데이터베이스_이름}} --result-file={{경로/대상/파일.sql}}`

- 특정 테이블을 백업하여 파일로 출력 (사용자에게 비밀번호가 요청됨):

`mysqldump --user {{사용자_명}} --password {{데이터베이스_이름}} {{테이블_이름}} > {{경로/대상/파일.sql}}`

- 모든 데이터베이스를 백업하여 파일로 출력 (사용자에게 비밀번호가 요청됨):

`mysqldump --user {{사용자_명}} --password --all-databases > {{경로/대상/파일.sql}}`

- 원격 호스트의 모든 데이터베이스를 백업하여 파일로 출력 (사용자에게 비밀번호가 요청됨):

`mysqldump --host={{IP_또는_호스트이름}} --user {{사용자_명}} --password --all-databases > {{경로/대상/파일.sql}}`
