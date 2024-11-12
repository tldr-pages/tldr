# Set-Date

> 컴퓨터의 시스템 시간을 지정한 시간으로 변경합니다.
> 이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/set-date>.

- 시스템 날짜에 3일 추가:

`Set-Date -Date (Get-Date).AddDays({{3}})`

- 시스템 시계를 10분 되돌리기:

`Set-Date -Adjust -0:10:0 -DisplayHint Time`

- 시스템 시계에 90분 추가:

`$90mins = New-TimeSpan -Minutes {{90}}; Set-Date -Adjust $90mins`
