# odps func

> ODPS (Open Data Processing Service)에서 함수 관리.
> 같이 보기: `odps`.
> 더 많은 정보: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

- 현재 프로젝트의 함수 표시:

`list functions;`

- `.jar` 리소스를 사용하여 Java 함수 생성:

`create function {{함수_이름}} as {{경로.대상.패키지.Func}} using '{{패키지.jar}}';`

- `.py` 리소스를 사용하여 Python 함수 생성:

`create function {{함수_이름}} as {{스크립트.Func}} using '{{스크립트.py}}';`

- 함수 삭제:

`drop function {{함수_이름}};`
