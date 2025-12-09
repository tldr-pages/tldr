# Get-Date

> 현재 날짜와 시간을 가져옵니다.
> 참고: 이 명령은 PowerShell을 통해서만 사용할 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-date>.

- 현재 날짜와 시간을 표시:

`Get-Date`

- .NET 형식 지정자로 현재 날짜와 시간 표시:

`Get-Date -Format "{{yyyy-MM-dd HH:mm:ss}}"`

- UTC 및 ISO 8601 형식으로 현재 날짜와 시간 표시:

`(Get-Date).ToUniversalTime()`

- 유닉스 타임스탬프 변환:

`Get-Date -UnixTimeSeconds {{1577836800}}`
