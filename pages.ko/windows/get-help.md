# Get-Help

> PowerShell 명령(별칭, cmdlet, 함수)에 대한 도움말 정보와 문서를 표시.
> 이 명령은 PowerShell을 통해서만 실행할 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/get-help>.

- 특정 PowerShell 명령에 대한 일반적인 도움말 정보 표시:

`Get-Help {{명령}}`

- 특정 PowerShell 명령에 대한 자세한 문서 표시:

`Get-Help {{명령}} -Detailed`

- 특정 PowerShell 명령에 대한 전체 기술 문서 표시:

`Get-Help {{명령}} -Full`

- 특정 PowerShell 명령의 특정 매개변수 문서만 표시 (가능한 경우 `*`을 사용하여 모든 매개변수 표시):

`Get-Help {{명령}} -Parameter {{매개변수}}`

- cmdlet의 예제만 표시 (가능한 경우):

`Get-Help {{명령}} -Examples`

- 사용 가능한 모든 cmdlet 도움말 페이지 나열:

`Get-Help *`

- `Update-Help`를 사용하여 현재 도움말 및 문서 지식베이스 업데이트:

`Update-Help`

- 기본 웹 브라우저에서 PowerShell 명령 문서의 온라인 버전 보기:

`Get-Help {{명령}} -Online`
