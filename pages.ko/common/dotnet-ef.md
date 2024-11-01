# dotnet ef

> Entity Framework Core용 디자인 타임 개발 작업 수행.
> 더 많은 정보: <https://learn.microsoft.com/ef/core/cli/dotnet>.

- 지정된 마이그레이션으로 데이터베이스 업데이트:

`dotnet ef database update {{마이그레이션}}`

- 데이터베이스 삭제:

`dotnet ef database drop`

- 사용 가능한 `DbContext` 유형 나열:

`dotnet ef dbcontext list`

- 데이터베이스에 대한 `DbContext` 및 엔티티 유형의 코드 생성:

`dotnet ef dbcontext scaffold {{연결_문자열}} {{프로바이더}}`

- 새 마이그레이션 추가:

`dotnet ef migrations add {{이름}}`

- 마지막 마이그레이션 제거 및 최신 마이그레이션에 대한 코드 변경 사항 롤백:

`dotnet ef migrations remove`

- 사용 가능한 마이그레이션 나열:

`dotnet ef migrations list`

- 마이그레이션 범위에서 SQL 스크립트 생성:

`dotnet ef migrations script {{시작_마이그레이션}} {{종료_마이그레이션}}`
