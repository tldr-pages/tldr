# Clear-RecycleBin

> 휴지통의 항목을 삭제.
> 이 명령은 PowerShell 버전 5.1 이하 또는 7.1 이상에서만 사용할 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/clear-recyclebin>.

- 휴지통의 모든 항목 삭제:

`Clear-RecycleBin`

- 특정 드라이브의 휴지통 삭제:

`Clear-RecycleBin -DriveLetter {{C}}`

- 추가 확인 없이 휴지통 삭제:

`Clear-RecycleBin -Force`
