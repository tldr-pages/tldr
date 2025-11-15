# odps inst

> ODPS(오픈 데이터 프로세싱 서비스)에서 인스턴스를 관리합니다.
> 같이 보기: `odps`.
> 더 많은 정보: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

- 현재 사용자가 생성한 인스턴스 보기:

`show instances;`

- 인스턴스의 세부 정보 설명:

`desc instance {{인스턴스_ID}};`

- 인스턴스 상태 확인:

`status {{인스턴스_ID}};`

- 인스턴스 종료를 대기하며 로그 및 진행 정보를 출력:

`wait {{인스턴스_ID}};`

- 인스턴스 종료:

`kill {{인스턴스_ID}};`
