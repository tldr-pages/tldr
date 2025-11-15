# tasklist

> 로컬 또는 원격 머신에서 현재 실행 중인 프로세스 목록을 표시합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/tasklist>.

- 현재 실행 중인 프로세스 표시:

`tasklist`

- 지정된 출력 형식으로 실행 중인 프로세스 표시:

`tasklist /fo {{표|목록|csv}}`

- 지정된 `.exe` 또는 `.dll` 파일 이름으로 실행 중인 프로세스 표시:

`tasklist /m {{모듈_패턴}}`

- 원격 머신에서 실행 중인 프로세스 표시:

`tasklist /s {{원격_이름}} /u {{사용자명}} /p {{암호}}`

- 각 프로세스에서 사용하는 서비스 표시:

`tasklist /svc`
