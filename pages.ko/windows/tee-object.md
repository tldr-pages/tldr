# Tee-Object

> 명령어 출력을 파일 또는 변수에 저장하고 파이프라인으로 전달합니다.
> 참고: 이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/tee-object>.

- 프로세스를 파일과 콘솔에 출력:

`Get-Process | Tee-Object -FilePath {{경로\대상\파일}}`

- 프로세스를 변수와 `Select-Object`에 출력:

`Get-Process notepad | Tee-Object -Variable {{proc}} | Select-Object processname,handles`
