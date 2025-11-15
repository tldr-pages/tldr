# wmic

> 실행 중인 프로세스에 대한 세부 정보를 보는 데 사용되는 대화형 쉘입니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/wmic>.

- 기본 문법:

`wmic {{별칭}} {{where_구문}} {{verb_구문}}`

- 현재 실행 중인 프로세스에 대한 간단한 세부 정보 표시:

`wmic process list brief`

- 현재 실행 중인 프로세스에 대한 전체 세부 정보 표시:

`wmic process list full`

- 프로세스 이름, 프로세스 ID 및 부모 프로세스 ID와 같은 특정 필드 접근:

`wmic process get {{이름,프로세스_id,부모_프로세스_id}}`

- 특정 프로세스에 대한 정보 표시:

`wmic process where {{이름="example.exe"}} list full`

- 특정 프로세스에 대한 특정 필드 표시:

`wmic process where processid={{프로세스_id}} get {{이름,명령어}}`

- 프로세스 종료:

`wmic process {{프로세스_id}} delete`
