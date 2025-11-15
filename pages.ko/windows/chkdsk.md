# chkdsk

> 파일 시스템 및 볼륨 메타데이터의 오류를 검사.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/chkdsk>.

- 검사할 드라이브 문자(콜론 포함), 마운트 지점 또는 볼륨 이름 지정:

`chkdsk {{볼륨}}`

- 특정 볼륨의 오류 수정:

`chkdsk {{볼륨}} /f`

- 검사 전에 특정 볼륨을 마운트 해제:

`chkdsk {{볼륨}} /x`

- 로그 파일 크기를 특정 크기로 변경 (NTFS 전용):

`chkdsk /l{{크기}}`
