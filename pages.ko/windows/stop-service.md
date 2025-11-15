# Stop-Service

> 실행 중인 서비스를 중지합니다.
> 참고: 이 명령은 PowerShell을 통해서만 사용할 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/stop-service>.

- 로컬 컴퓨터의 서비스 중지:

`Stop-Service -Name {{서비스_이름}}`

- 표시 이름을 사용하여 서비스 중지:

`Stop-Service -DisplayName "{{이름}}"`

- 종속 서비스가 있는 서비스 중지:

`Stop-Service -Name {{서비스_이름}} -Force -Confirm`
