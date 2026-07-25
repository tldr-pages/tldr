# compact

> NTFS 파티션의 파일 및 디렉터리 압축 상태를 확인하거나 변경.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/compact>.

- 현재 디렉터리의 파일 압축 상태 표시:

`compact`

- 지정한 파일 압축:

`compact /c {{경로\대상\파일}}`

- 지정한 파일 압축 해제:

`compact /u {{경로\대상\파일}}`

- 디렉터리와 모든 하위 디렉터리의 파일 압축:

`compact /c /s {{경로\대상\디렉터리}}`

- 디렉터리와 모든 하위 디렉터리의 파일 압축 해제:

`compact /u /s {{경로\대상\디렉터리}}`
