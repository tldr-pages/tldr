# csvsql

> CSV 파일에 대한 SQL문을 생성하거나 해당 문을 데이터베이스에서 직접 실행.
> csvkit에 포함됨.
> 더 많은 정보: <https://csvkit.readthedocs.io/en/latest/scripts/csvsql.html>.

- CSV 파일에 대한 `CREATE TABLE` SQL 문을 생성:

`csvsql {{경로/대상/데이터.csv}}`

- CSV 파일을 SQL 데이터베이스로 가져옴:

`csvsql --insert --db "{{mysql://user:password@host/database}}" {{데이터.csv}}`

- CSV 파일에서 SQL 쿼리를 실행:

`csvsql --query "{{select * from 'data'}}" {{데이터.csv}}`
