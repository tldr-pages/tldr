# Start-Service

> 중지된 서비스를 시작합니다.
> 참고: 이 명령은 PowerShell을 통해서만 사용할 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/start-service>.

- 서비스 이름을 사용하여 서비스 시작:

`Start-Service -Name {{서비스_이름}}`

- 서비스를 시작하지 않고 정보 표시:

`Start-Service -DisplayName *{{이름}}* -WhatIf`

- 비활성화된 서비스 시작:

`Set-Service {{서비스_이름}} -StartupType {{manual}}; Start-Service {{서비스_이름}}`
