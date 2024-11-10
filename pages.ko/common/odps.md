# odps

> Aliyun ODPS (Open Data Processing Service) 명령줄 도구.
> `inst`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
> 더 많은 정보: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

- 사용자 지정 구성 파일로 명령줄 시작:

`odpscmd --config={{odps_config.ini}}`

- 현재 프로젝트 변경:

`use {{프로젝트_이름}};`

- 현재 프로젝트의 테이블 표시:

`show tables;`

- 테이블 설명:

`desc {{테이블_이름}};`

- 테이블 파티션 표시:

`show partitions {{테이블_이름}};`

- 파티션 설명:

`desc {{테이블_이름}} partition ({{파티션_명세}});`
