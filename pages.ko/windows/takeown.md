# takeown

> 파일 또는 디렉토리의 소유권을 가져옵니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/takeown>.

- 지정된 파일의 소유권을 취득:

`takeown /f {{경로\대상\파일}}`

- 지정된 디렉토리의 소유권을 취득:

`takeown /d {{경로\대상\디렉토리}}`

- 지정된 디렉토리 및 모든 하위 디렉토리의 소유권을 취득:

`takeown /r /d {{경로\대상\디렉토리}}`

- 현재 사용자 대신 관리자 그룹의 소유권으로 변경:

`takeown /a /f {{경로\대상\파일}}`
