# Get-Command

> 현재 PowerShell 세션에서 사용 가능한 명령을 나열하고 가져옴.
> 이 명령은 PowerShell을 통해서만 실행 가능.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/get-command>.

- 현재 컴퓨터에서 사용 가능한 모든 PowerShell 명령(별칭, cmdlet, 함수) 나열:

`Get-Command`

- 현재 세션에서 사용 가능한 모든 PowerShell 명령 나열:

`Get-Command -ListImported`

- 컴퓨터에서 사용 가능한 PowerShell 별칭/cmdlet/함수만 나열:

`Get-Command -Type {{별칭|Cmdlet|함수}}`

- 현재 세션에서 PATH에 있는 프로그램이나 명령만 나열:

`Get-Command -Type Application`

- 모듈 이름으로 PowerShell 명령만 나열, 예: 유틸리티 관련 명령은 `Microsoft.PowerShell.Utility`:

`Get-Command -Module {{모듈}}`

- 이름으로 명령 정보(예: 버전 번호나 모듈 이름) 가져오기:

`Get-Command {{명령}}`
