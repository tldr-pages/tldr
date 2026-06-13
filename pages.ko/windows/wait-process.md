# Wait-Process

> 더 많은 입력을 수락하기 전에 프로세스가 중지될 때까지 기다립니다.
> 참고: 이 명령은 PowerShell을 통해서만 사용할 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/wait-process>.

- 프로세스 중지 및 기다리기:

`Stop-Process -Id {{프로세스_아이디}}; Wait-Process -Id {{프로세스_아이디}}`

- 지정된 시간 동안 프로세스 기다리기:

`Wait-Process -Name {{프로세스_이름}} -Timeout {{30}}`
