# odps auth

> ODPS (Open Data Processing Service)에서 사용자 권한 관리.
> 같이 보기: `odps`.
> 더 많은 정보: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

- 현재 프로젝트에 사용자 추가:

`add user {{사용자명}};`

- 사용자에게 권한 집합 부여:

`grant {{작업_목록}} on {{객체_유형}} {{객체_이름}} to user {{사용자명}};`

- 사용자의 권한 보기:

`show grants for {{사용자명}};`

- 사용자 역할 생성:

`create role {{역할_이름}};`

- 역할에 권한 집합 부여:

`grant {{작업_목록}} on {{객체_유형}} {{객체_이름}} to role {{역할_이름}};`

- 역할의 권한 설명:

`desc role {{역할_이름}};`

- 사용자에게 역할 부여:

`grant {{역할_이름}} to {{사용자명}};`
