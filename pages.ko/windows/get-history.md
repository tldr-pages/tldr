# Get-History

> PowerShell 명령 히스토리 표시.
> 참고: 이 명령은 PowerShell을 통해서만 사용할 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/get-history>.

- ID와 함께 명령 히스토리 목록 표시:

`Get-History`

- ID로 PowerShell 히스토리 항목 가져오기:

`Get-History -Id {{id}}`

- 마지막 N개의 명령 표시:

`Get-History -Count {{10}}`
