# odps resource

> ODPS(Open Data Processing Service)에서 리소스를 관리.
> 같이 보기: `odps`.
> 더 많은 정보: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

- 현재 프로젝트의 리소스 표시:

`list resources;`

- 파일 리소스 추가:

`add file {{파일명}} as {{별칭}};`

- 아카이브 리소스 추가:

`add archive {{아카이브.tar.gz}} as {{별칭}};`

- .jar 리소스 추가:

`add jar {{패키지.jar}};`

- .py 리소스 추가:

`add py {{스크립트.py}};`

- 리소스 삭제:

`drop resource {{리소스_이름}};`
