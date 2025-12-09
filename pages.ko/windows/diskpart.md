# diskpart

> 디스크, 볼륨 및 파티션 관리 도구.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/diskpart>.

- 관리 명령 프롬프트에서 diskpart를 실행하여 명령줄에 진입:

`diskpart`

- 모든 디스크 나열:

`list disk`

- 볼륨 선택:

`select volume {{볼륨}}`

- 선택된 볼륨에 드라이브 문자 할당:

`assign letter {{문자}}`

- 새 파티션 생성:

`create partition primary`

- 선택된 볼륨 활성화:

`active`

- diskpart 종료:

`exit`
